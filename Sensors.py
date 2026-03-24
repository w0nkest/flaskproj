from SmartThing import *
from random import randint
import time


class Temperature(SmartThing):
    def __init__(self, id: int, location: str, temp: float=randint(-30, 30)):
        super().__init__(id, location)
        self.temp = temp

    def check_connection(self) -> str:
        super().check_connection()
        return 'Temperature sensor is connected!' if self.connect else 'Temperature sensor is not connected'

    def update_info(self) -> str:
        super().update_info()
        return f'Now temperature reached {self.temp}'

    def draw_precipitations(self):
        print('Precipitations will be drawn')

    def send_data(self):
        print('Data from temperature will be sent')

    def request_data(self):
        print('Data from temperature will be requested')


class Time(SmartThing):
    def __init__(self, id: int, location: str, currenttime: str=str(time.time())):
        super().__init__(id, location)
        self.currenttime = currenttime

    def check_connection(self) -> str:
        super().check_connection()
        return 'Clock is connected!' if self.connect else 'Clock is not connected'

    def update_info(self) -> str:
        super().update_info()
        return f'Now is {self.currenttime}'

    def request_data(self):
        print('Data from time will be requested')

    def send_data(self):
        print('Data from time will be sent')


