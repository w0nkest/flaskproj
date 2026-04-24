from models.Sensors import *
from models.BusStation import *
from models.Bus import *

class MainControlUnit:
    """
    Class MainControlUnit is designed for connecting
    different smart devices in one place
    """
    def __init__(self):
        """
            Class MainControlUnit constructor
        """
        self.times = list[Time]()
        self.temps = list[Temperature]()
        self.buses = list[Bus]()
        self.busstations = list[BusStation]()

    def add_device(self, device):
        """
        Add a device to the MainControlUnit
        :param device: takes device, which type is in (Time, Temperature, BusStation, Bus)
        """
        if type(device) == Time: self.times.append(device)
        elif type(device) == Temperature: self.temps.append(device)
        elif type(device) == Bus: self.busstations.append(device)
        elif type(device) == BusStation: self.busstations.append(device)
        else: print('Device type is not in allowed list')

    def receive_data_from(self, device):
        """
        Receive data from device
        :param device: takes device, which type is in (Time, Temperature, BusStation, Bus)
        :return: data from device, linked in method as param
        """
        if type(device) == Time: return device.send_data()
        elif type(device) == Temperature: return device.send_data()
        elif type(device) == Bus: return device.send_GPS()
        elif type(device) == BusStation: return device.send_data()
        else: return 'Device type is not in allowed list'

    def receive_data(self):
        """
        Receive data from all devices, linked in MainControlUnit
        :return: 4 lists containing data in order (time_data, temp_data, bus_data, busstaion_data)
        """
        time_data, temp_data, bus_data, busstation_data = (
            [t.send_data() for t in self.times], [t.send_data() for t in self.temps],
            [t.send_GPS() for t in self.buses], [t.send_data() for t in self.busstations])

        return time_data, temp_data, bus_data, busstation_data