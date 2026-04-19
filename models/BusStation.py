from models.Sensors import *

class BusStation(SmartThing):
    """
    BusStation obj
    """
    def __init__(self, id: int, location: str, coords: tuple[float, float], clock: Time,
                 temp: Temperature, buses=None):
        """
        Constructor
        :param id: index
        :param location: string, containing location
        :param clock: Time, connected clock
        :param temp: Temperature, connected temperature sensor
        :param buses: list of Bus - creates list of tuples (bus, state), state can be either far or near
        """
        super().__init__(id, location)
        self.clock = clock
        self.temp = temp
        self._buses = [(bus, 'far') for bus in buses] if buses is not None else []
        self.coords = coords

    def add_bus(self, bus):
        self._buses.append((bus, 'far'))

    def update_waitingtimes(self):
        """
        Updates state of buses, connected to this station
        """
        def compare_coords(static: tuple[float, float], moving: tuple[float, float]) -> float:
            return ((static[0] - moving[0]) ** 2 + (static[1] - moving[1]) ** 2) ** 0.5

        for i, (bus, state) in enumerate(self._buses):
            if compare_coords((bus.lat, bus.lon), self.coords) < 0.015:
                self._buses[i] = (bus, 'near')
            else:
                self._buses[i] = (bus, 'far')

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
            'waiting_times': dict([(bus.route, state) for bus, state in self._buses])
        }
        return data