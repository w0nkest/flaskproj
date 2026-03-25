from flask import Flask, render_template, jsonify
from tools.devcheck import *

app = Flask(__name__)

@app.route('/')
def connectionchecking():
    time = Time(1, 'somewhere')
    temp = Temperature(1, 'somewhere')
    bs = BusStation(1, 'somewhere', time, temp)
    bus = Bus('4', [bs])

    for creature in (time, temp, bs):
        print('\nChecking', type(creature))
        connection(creature)
        check_connection(creature)
        check_send_data(creature)
        check_request_data(creature)
        check_update_info(creature)
        if type(creature) is Temperature: check_temperature(creature)
        if type(creature) is BusStation: check_waitingtimes(creature)

    print('\nChecking', type(bus), '\n')
    check_bus(bus)

    timec, tempc, bsc, busc = (time.check_connection(), temp.check_connection(),
                               bs.check_connection(), bus.check_connection())

    return render_template('connections.html', time=timec, temp=tempc, bs=bsc, bus=busc)

@app.route('/status')
def get_station_status():
    
    time_sensor = Time(101, 'Фитнес-Хаус на Блюхера')
    temp_sensor = Temperature(201, 'Фитнес-Хаус на Блюхера')
    station = BusStation(6, 'Фитнес-Хаус на Блюхера', time_sensor, temp_sensor)
    
    station.connection()
    time_sensor.connection()
    temp_sensor.connection()
    station.update_info()
    
    result = station.send_data()
     
    return render_template('station_status.html', data = result)


if __name__ == '__main__':
    app.run()