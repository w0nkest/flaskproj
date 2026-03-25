from Sensors import *
from BusStation import *

class MainControlUnit:
    def __init__(self):
        self.times = list[Time]()
        self.temps = list[Temperature]()
        self.buses = list[Bus]()
        self.busstations = list[BusStation]()

    def add_device(self, device):
        if type(device) == Time: self.times.append(device)
        elif type(device) == Temperature: self.temps.append(device)
        elif type(device) == Bus: self.busstations.append(device)
        elif type(device) == BusStation: self.busstations.append(device)
        else: print('Device type is not in allowed list')

    def receive_data_from(self, device):
        if type(device) == Time: return device.send_data()
        elif type(device) == Temperature: return device.send_data()
        elif type(device) == Bus: return device.send_GPS()
        elif type(device) == BusStation: return device.send_data()
        else: print('Device type is not in allowed list')

    def receive_data(self):
        time_data, temp_data, bus_data, busstation_data = (
            [t.send_data() for t in self.times], [t.send_data() for t in self.temps],
            [t.send_GPS() for t in self.buses], [t.send_data() for t in self.busstations])

        return time_data, temp_data, bus_data, busstation_data