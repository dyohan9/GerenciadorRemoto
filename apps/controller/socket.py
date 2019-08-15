from twisted.internet import reactor, protocol


class MyClient(protocol.Protocol):
    def __init__(self):
        self.connected = False

    def connectionMade(self):
        if not self.connected:
            self.connected = True
        else:
            self.transport.write(self.factory.arg.encode('utf-8'))

    def dataReceived(self, data):
        packet = str(data.decode('utf-8'))[2::][:-1:]
        print(packet)


class MyClientFactory(protocol.ClientFactory):
    protocol = MyClient

    def __init__(self, arg):
        self.arg = arg
