class CRP:
    def __init__(self):
        self.state = 'CLOSED'

    def bind(self, addr):
        self.src_host = addr[0]
        self.src_port = addr[1]
        self.state = 'LISTENING'

crp = CRP()
crp.bind(('192.168.1.1', 5000))
