from models.BusStation import *
from models.SmartThing import *

def check_send_data(creature: SmartThing):
    """
    Checks send_data method of device
    :param creature: takes SmartThing or SmartThing's child object
    """
    creature.send_data()

def connection(creature: SmartThing):
    """
    Checks connection method of device, and establishing the connection to device
    :param creature: takes SmartThing or SmartThing's child object
    """
    creature.connection()

def check_connection(creature: SmartThing):
    """
    Checks check_connection method of device
    :param creature: takes SmartThing or SmartThing's child object
    """
    creature.check_connection()

def check_update_info(creature: SmartThing):
    """
    Checks update_info method of device
    :param creature: takes SmartThing or SmartThing's child object
    """
    creature.update_info()

def check_request_data(creature: SmartThing):
    """
    Checks request_data method of device
    :param creature: takes SmartThing or SmartThing's child object
    """
    creature.request_data()

def check_temperature(creature: Temperature):
    """
    Checks draw_precipitations method of Temperature sensor
    :param creature: takes device, which type is Temperature
    """
    creature.draw_precipitations()

def check_waitingtimes(creature: BusStation):
    """
    Checks update_waitingtimes method of BusStation sensor
    :param creature: takes device, which type is BusStation
    """
    creature.update_waitingtimes()

def check_bus(creature: Bus):
    """
    Checks all Bus methods
    :param creature: takes device, which type is Bus
    """
    creature.connection()
    creature.check_connection()
    creature.send_GPS()
    creature.update_route_screen()