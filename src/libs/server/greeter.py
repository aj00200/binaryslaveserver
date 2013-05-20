'''
Handle connections from a client greeter. Provide information such as
sub-servers and news.
'''
import asyncore
import socket
import struct


class Handler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(1)
        if data == b'\x00':
            # TODO: load alternate server names from the config
            self.send(struct.pack('16s16s16s16s', b'localhost', b'localhost',
                                  b'localhost', b'localhost'))
        elif data == b'\x01':
            self.send(b'Welcome to the new world')


class Server(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accepted(self, sock, addr):
        handler = Handler(sock)
