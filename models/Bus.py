from models.BusStation import BusStation
import random

class Bus:
    """
    Bus creature
    """
    def __init__(self, route: str, stations: list[BusStation], coords: tuple[float, float]):
        """
        Constructor
        :param route: str, number of route
        :param stations: list of BusStation
        """
        self.route = route
        self.stations = stations
        self.connect = False
        self.lat, self.lon = coords

    def update_stations(self):
        for station in self.stations:
            station.update_waitingtimes()

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

            self.update_stations()

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

            self.update_stations()
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