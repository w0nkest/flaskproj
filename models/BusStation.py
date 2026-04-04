from models.SmartThing import *
from models.Sensors import *
import random

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

    def send_data(self, request):
        """
        Receives some data
        """
        print('Data will be sent')
        self.clock.send_data(request)
        self.temp.send_data(request)



    def update_info(self) -> str:
        """
        Обновляет данные на всех датчиках остановки
        :return: string с подтверждением обновления
        """
        self.clock.update_info()
        self.temp.update_info()
        return f'All sensors for station {self.location} (ID: {self.id}) have been updated.'

    def request_data(self) -> dict:
        """
        Собирает данные со всех подключенных датчиков в один пакет
        :return: dict: { station_id, location, status,
        sensors_data { clock, temperature }, waiting_times }
        """
        print(f'Sending aggregated data from Bus Station: {self.location}')

        data = {
            'station_id': self.id,
            'location': self.location,
            'status': 'Online' if self.connect else 'Offline',
            'sensors_data': {
                'clock': self.clock.request_data(),
                'temperature': self.temp.request_data()
            },
            'waiting_times': self.waittimes
        }
        return data


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
        self.lat = 59.9343
        self.lon = 30.3351

    def connection(self):
        """
        Establishes connection
        """
        self.connect = True
        print(f'Bus {self.route} connected to GPS')

    def check_connection(self) -> str:
        """
        Checks connection
        :return: string, state of connection
        """
        return 'Bus is connected' if self.connect else 'Bus is not connected'

    def update_route_screen(self):
        """
        Updates route screen and GPS data
        """
        if self.connect:
            self.lat += random.uniform(-0.001, 0.001)
            self.lon += random.uniform(-0.001, 0.001)
            return f"Bus {self.route} is moving..."
        return "Bus is offline"

    def send_GPS(self, request):
        """
        Receives GPS data
        :param request: json object
        :return:
        """
        requestdata = (request.args.get('lat'), request.args.get('lon'))
        try:
            requestdata = map(float, requestdata)
            self.lat, self.lon = requestdata
        except:
            self.update_route_screen()

    def request_data(self) -> dict:
        """
        Sends Bus data data
        :return: dict: { route, lat, lon, status }
        """
        return {
            'route': self.route,
            'lat': round(self.lat, 4),
            'lon': round(self.lon, 4),
            'status': 'In route' if self.connect else 'In depot'
        }

    def request_GPS(self) -> dict:
        """
        Sends GPS data
        :return: dict: { lat, lon }
        """
        return {
            'lat': round(self.lat, 4),
            'lon': round(self.lon, 4),
        }