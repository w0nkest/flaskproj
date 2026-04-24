import pymongo
import datetime

class Logger:
    def __init__(self, db_name: str):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
        self.last_temperature = None

    def log_temperature(self, value: float):
        if value != self.last_temperature:
            self.last_temperature = value
            record = {
                'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'temperature': value
            }
            return self.db['temperature_log'].insert_one(record)
        else:
            print('Температура не изменилась, запись не добавлена')

    def log_bus_position(self, route: str, lat: float, lon: float):
        record = {
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'route': route,
            'lat': lat,
            'lon': lon
        }
        return self.db['bus_position_log'].insert_one(record)