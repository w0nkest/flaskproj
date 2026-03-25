from SmartThing import *
from Sensors import *

class BusStation(SmartThing):
    def __init__(self, id: int, location: str, clock: Time, temp: Temperature):
        super().__init__(id, location)
        self.clock = clock
        self.temp = temp
        self.waittimes = list()

    def update_waitingtimes(self):
        print('Waiting times will be updated')

    def check_connection(self) -> str:
        super().check_connection()
        return 'Bus station is connected!' if self.connect else 'Bus station is not connected'

    def send_data(self):
        print('Data from bus station will be sent')

    def update_info(self) -> str:
        return f'{self.clock.update_info()}\n{self.temp.update_info()}'

    def request_data(self):
        print('Data from bus station will be requested')


class Bus:
    def __init__(self, route: str, stations: list[BusStation]):
        self.route = route
        self.stations = stations
        self.connect = False

    def connection(self):
        self.connect = True
        print('Connect established')

    def check_connection(self) -> str:
        return 'Bus is connected' if self.connect else 'Bus is not connected'

    def update_route_screen(self):
        print('Route screen will be updated')

    def send_GPS(self):
        print('GPS will be sent')