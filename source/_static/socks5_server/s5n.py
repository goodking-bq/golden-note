import socket
import asyncio
from struct import pack, unpack
import argparse

has_uvloop = False
try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except:
    pass


class UdpClient(asyncio.DatagramProtocol):
    def __init__(self, server_transport, client_ip):
        self.server_transport = server_transport
        self.client_ip = client_ip
        self.client_port = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        if self.client_ip == addr[0]:  # 从客户端来的数据
            self.client_port = addr[1]
            addr_type, dest_addr, dest_port, header_length = self._parse_header(data[3:])
            _data = data[3 + header_length:]
            if dest_port and dest_addr:
                self.transport.sendto(_data, (dest_addr, dest_port))
            else:
                return
        else:
            host = unpack("!I", socket.inet_aton(self.client_ip))[0]
            header = pack('!BBBBIH', 0x00, 0x00, 0x00, 0x01, host, int(self.client_port))
            data = header + data
            self.transport.sendto(data, (self.client_ip, self.client_port))

    def connection_lost(self, exc):
        self.server_transport.close()

    def _parse_header(self, data):
        addrtype = data[0]
        dest_addr = None
        dest_port = None
        header_length = 0
        if addrtype == 1:  # IPV4
            dest_addr = socket.inet_ntoa(data[1:5])
            dest_port = unpack('>H', data[5:7])[0]
            header_length = 7
        elif addrtype == 3:  # DOMAIN
            addrlen = data[1]
            dest_addr = data[2:2 + addrlen]
            dest_port = unpack('>H', data[2 + addrlen:4 + addrlen])[0]
            header_length = 4 + addrlen
        elif addrtype == 4:
            dest_addr = socket.inet_ntop(socket.AF_INET6, data[1:17])
            dest_port = unpack('>H', data[17:19])[0]
            header_length = 19
        else:
            pass
        return addrtype, dest_addr, dest_port, header_length


class Client(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.server_transport = None

    def data_received(self, data):
        self.server_transport.write(data)

    def connection_lost(self, *args):
        self.server_transport.close()


class Server(asyncio.Protocol):
    UDP = False
    loop = asyncio.get_event_loop()
    FROM = None
    state = None
    transport = None

    def __init__(self, user=None, password=None):
        self.USER = user
        self.PASSWORD = password

    def connection_made(self, transport):
        self.FROM = transport.get_extra_info('peername')
        self.transport = transport  # 本身的
        self.state = 'init'

    def connection_lost(self, exc):
        self.transport.close()

    def init(self, data):
        assert data[0] == 0x05
        if self.USER and self.PASSWORD:
            self.transport.write(pack('!BB', 0x05, 0x02))  # user/password auth
            self.state = 'auth'
        else:
            self.transport.write(pack('!BB', 0x05, 0x00))  # no auth
            self.state = 'host'

    def auth(self, data):
        _auth = None
        if self.USER and self.PASSWORD:
            _auth = b'\x06%s\x06%s' % (self.USER, self.PASSWORD)
        if data[1:] == _auth:
            self.transport.write(pack('!BB', 0x01, 0x00))
            self.state = 'host'
        else:
            self.transport.write(pack('!BB', 0x01, 0x01))

    def host(self, data):
        ver, cmd, rsv, atype = data[:4]
        assert ver == 0x05
        if cmd == 0x01:  # CONNECT模式
            feture = self.connect
        elif cmd == 0x03:  # udp 模式的
            feture = self.udp
            self.UDP = True
        if atype == 3:  # domain
            length = data[4]
            hostname, nxt = data[5:5 + length], 5 + length
        elif atype == 1:  # ipv4
            hostname, nxt = socket.inet_ntop(socket.AF_INET, data[4:8]), 8
        elif atype == 4:  # ipv6
            hostname, nxt = socket.inet_ntop(socket.AF_INET6, data[4:20]), 20
        port = unpack('!H', data[nxt:nxt + 2])[0]
        asyncio.ensure_future(feture(hostname, port))
        self.state = 'data'

    def data(self, data):
        self.client_transport.write(data)

    def data_received(self, data):
        func = getattr(self, self.state)
        func(data)

    async def connect(self, hostname, port):
        transport, client = await self.loop.create_connection(Client, hostname, port)
        client.server_transport = self.transport
        self.client_transport = transport
        hostip, port = transport.get_extra_info('sockname')
        host = unpack("!I", socket.inet_aton(hostip))[0]
        self.transport.write(
            pack('!BBBBIH', 0x05, 0x00, 0x00, 0x01, host, port))

    async def udp(self, hostname, port):
        # transport, client = await self.loop.create_connection(UdpClient, hostname, port)
        transport, client = await self.loop.create_datagram_endpoint(
            lambda: UdpClient(self.transport, self.FROM[0]), local_addr=(hostname, port))
        hostip, port = transport.get_extra_info('sockname')
        host = unpack("!I", socket.inet_aton(hostip))[0]
        self.transport.write(
            pack('!BBBBIH', 0x05, 0x00, 0x00, 0x01, host, port))  # 回写


def main(auth, host, port):
    loop = asyncio.get_event_loop()
    srv = loop.create_server(lambda: Server(auth), host, int(port))
    loop.run_until_complete(srv)
    loop.run_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='使用asyncio的socks5服务器')
    server_group = parser.add_argument_group('server arguments')
    server_group.add_argument('-b', '--bind', dest='bind', default='0.0.0.0:8888', help='绑定的ip')
    server_group.add_argument('-u', '--user', dest='user', help='认证的用户名')
    server_group.add_argument('-p', '--password', dest='password', help='认证的密码')
    parser.add_argument('-v', '--version', default='0.1')
    args = parser.parse_args()
    if args.user and args.password:
        auth = (args.user, args.password,)
    else:
        auth = None
    host, port = args.bind.split(':')
    main(auth, host, int(port))
