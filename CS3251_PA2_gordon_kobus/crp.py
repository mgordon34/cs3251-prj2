import socket

class CRP:
    def __init__(self):
        self.state = 'CLOSED'
        self.mode = None
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def bind(self, addr):
        self.src_addr = addr
        self.src_host = addr[0]
        self.src_port = addr[1]
        self.sock.bind(addr)
        self.state = 'LISTEN'

    def listen(self):
        if self.state != 'LISTEN':
            print('wrong state!')
            self.sock.close()
            exit(1)
        self.mode = 'SERVER'

    def connect(self, addr):
        if self.state != 'CLOSED':
            print('wrong state!')
            self.sock.close()
            exit(1)
        self.mode = 'CLIENT'

        self.dest_addr = addr
        self.dest_host = addr[0]
        self.dest_port = addr[1]
        #TODO: handshake happens here

        # after handshake established
        self.state = 'ESTABLISHED'
        return

    def accept(self):
        if self.state != 'LISTEN':
            print('wrong state!')
            self.sock.close()
            exit(1)
        if self.mode != 'SERVER':
            print('not in server mode!')
            self.sock.close()
            exit(1)

        message, addr = self.sock.recvfrom(4096) #idk what our buffer size should be

        ret = self._handle(message)
        if ret != 0:
            print('error: ' + ret)
            self.sock.close()
            exit(1)

        self.state = 'ESTABLISHED'


    def _handle(self, message):
        """
        Helper method to handle incoming messages from UDP. Various states will
        determine how to handle the message
        """
        if self.state == 'LISTEN':
            #TODO: handle handshake, maybe a _handshake method

            # after successful handshake
            return 0


    ### Helper method to send message over UDP encapsulated in CRP header data
    def _send(self, message, flags, addr):
        """
        Helper method to send message over UDP with header data included
        """
        #TODO: create header, add data, send message over UDP

crp = CRP()
crp.bind(('localhost', 5000))
crp.listen()
print(crp.state)
