from SmartThing import *
from Sensors import *

class BusStation(SmartThing):
    """
    BusStation obj
    """
    def __init__(self, id: int, location: str, clock: Time, temp: Temperature):
        """
        Constructor
        :param id: index
        :param location: string, containing location
        :param clock: Time, connected clock
        :param temp: Temperature, connected temperature sensor
        """
        super().__init__(id, location)
        self.clock = clock
        self.temp = temp
        self.waittimes = list()

    def update_waitingtimes(self):
        """
        Updates waiting times list
        """
        print('Waiting times will be updated')

    def check_connection(self) -> str:
        """
        Checks connection
        :return: string, state of connection
        """
        super().check_connection()
        return 'Bus station is connected!' if self.connect else 'Bus station is not connected'

    def send_data(self):
        """
        Sends data
        :return: -list, contains time, temp, location, waiting times...-
        """
        print('Data from bus station will be sent')

    def update_info(self) -> str:
        """
        Updates info of sensors
        :return: string, clock time, current temp
        """
        return f'{self.clock.update_info()}\n{self.temp.update_info()}'

    def request_data(self):
        """
        Requests some data
        """
        print('Data from bus station will be requested')


class Bus:
    """
    Bus creature
    """
    def __init__(self, route: str, stations: list[BusStation]):
        """
        Constructor
        :param route: str, number of route
        :param stations: list of BusStation
        """
        self.route = route
        self.stations = stations
        self.connect = False

    def connection(self):
        """
        Establishes connection
        """
        self.connect = True
        print('Connect established')

    def check_connection(self) -> str:
        """
        Checks connection
        :return: string, state of connection
        """
        return 'Bus is connected' if self.connect else 'Bus is not connected'

    def update_route_screen(self):
        """
        Updates route screen
        """
        print('Route screen will be updated')

    def send_GPS(self):
        """
        Sends GPS data
        :return: string: GPS
        """
        print('GPS will be sent')