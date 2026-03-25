from models.SmartThing import *
from random import randint
import time


class Temperature(SmartThing):
    """
    Temperature class, creates Temperature sensor
    """
    def __init__(self, id: int, location: str, temp: float=randint(-30, 30)):
        """
        Constructor
        :param id: index
        :param location: where is sensor located
        :param temp: takes temperature as param, unnecessary, if not given takes random number between -30 and 30
        """
        super().__init__(id, location)
        self.temp = temp

    def check_connection(self) -> str:
        """
        Checks connection to device
        :return: string, status of connection
        """
        super().check_connection()
        return 'Temperature sensor is connected!' if self.connect else 'Temperature sensor is not connected'

    def update_info(self) -> str:
        """
        Gets current temperature info
        :return: string, contains temperature
        """
        super().update_info()
        # Симуляция изменения температуры
        variation = randint(-2, 2)
        self.temp += variation
        # Мы в хорошем климатическом поясе
        if self.temp < -40: self.temp = -40
        if self.temp > 40: self.temp = 40
        return f'Now temperature reached {self.temp}'

    def draw_precipitations(self):
        """
        Selects precipitation picture
        """
        print('Precipitations will be drawn')

    def send_data(self) -> dict:
        """
        Sends current data
        :return: -list, contains temp, location...-
        """
        # Данные в формате словаря для API
        print(f'Sending temperature data from {self.location}')
        return {
            'sensor_id': self.id,
            'type': 'temperature',
            'value': self.temp,
            'unit': 'Celsius',
            'location': self.location
        }

    def request_data(self):
        """
        Request some data
        """
        print('Data from temperature will be requested')


class Time(SmartThing):
    """
    Time class, creates Time sensor - clock
    """
    def __init__(self, id: int, location: str, currenttime: str=time.strftime("%H:%M:%S")):
        """
        Constructor
        :param id: index
        :param location: where is sensor located
        :param currenttime: unnecessary, takes time in string format
        """
        super().__init__(id, location)
        self.currenttime = currenttime

    def check_connection(self) -> str:
        """
        Checks connection to device
        :return: string, state of connection
        """
        super().check_connection()
        return 'Clock is connected!' if self.connect else 'Clock is not connected'

    def update_info(self) -> str:
        """
        Gets current time
        :return: string containing current time
        """
        super().update_info()
        self.currenttime = time.strftime("%H:%M:%S") # Выводим актуальное время
        return f'Now is {self.currenttime}'

    def request_data(self):
        """
        Request some data
        """
        print('Data from time will be requested')

    def send_data(self) -> dict:
        """
        Sends current data
        :return: -list, contains time, location...-
        """
        print(f'Sending time data from {self.location}')
        return {
            'sensor_id': self.id,
            'type': 'clock',
            'value': self.currenttime,
            'location': self.location
        }


