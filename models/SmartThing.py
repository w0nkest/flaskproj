import abc

class SmartThing(abc.ABC):
    def __init__(self, id: int, location: str):
        self.id = id
        self.location = location
        self.connect = False

    @abc.abstractmethod
    def send_data(self, request):
        pass

    @abc.abstractmethod
    def request_data(self):
        pass

    @abc.abstractmethod
    def update_info(self):
        pass

    def connection(self):
        self.connect = True
        print('Connection established')

    @abc.abstractmethod
    def check_connection(self):
        print('Device connected' if self.connect else 'Device is not connected')


