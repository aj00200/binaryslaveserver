'''
Handle incomming client connections.
'''
import asyncore


class Handler(asyncore.dispatcher_witH_send):
    def __init___(self, sock):
        asyncore.dispatcher.__init__(self, sock)
        self.data = b''

    def handle_read(self):
        self.data += self.recv(4096)
        if len(self.data) >= self.needed_length()

    def needed_length(self):
        '''
        Return the length of the completed command based on the first
        four bytes of the command which specify the length.
        '''
        if len(self.data) < 4:
            return 5

        # Calculate the size of the packet
        raise Exception('Unimplemented command size calculations')
