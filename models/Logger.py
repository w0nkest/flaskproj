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
    
    def get_temperature_stats(self):
        cursor = self.db['temperature_log'].find({}, {'_id': 0, 'temperature': 1})
        temps = [doc['temperature'] for doc in cursor]
        if not temps:
            return None
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        return {'avg': round(avg_temp, 2), 'max': round(max_temp, 2)}

    def get_bus_position_count(self):
        return self.db['bus_position_log'].count_documents({})

    def get_last_bus_position(self):
        last = self.db['bus_position_log'].find_one(sort=[('_id', -1)])
        if last:
            return {
                'route': last.get('route'),
                'lat': last.get('lat'),
                'lon': last.get('lon'),
                'timestamp': last.get('timestamp')
            }
        return None
    
    def get_temperature_history(self):
        cursor = self.db['temperature_log'].find({}, {'_id': 0}).sort('timestamp', 1)
        labels = []
        data = []
        for doc in cursor:
            labels.append(doc['timestamp'])
            data.append(doc['temperature'])
        return {'labels': labels, 'data': data}