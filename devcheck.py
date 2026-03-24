from Sensors import *
from BusStation import *
from SmartThing import *

def check_send_data(creature: SmartThing):
    creature.send_data()

def connection(creature: SmartThing):
    creature.connection()

def check_connection(creature: SmartThing):
    creature.check_connection()

def check_update_info(creature: SmartThing):
    creature.update_info()

def check_request_data(creature: SmartThing):
    creature.request_data()

def check_temperature(creature: Temperature):
    creature.draw_precipitations()

def check_waitingtimes(creature: BusStation):
    creature.update_waitingtimes()

def check_bus(creature: Bus):
    creature.connection()
    creature.check_connection()
    creature.send_GPS()
    creature.update_route_screen()