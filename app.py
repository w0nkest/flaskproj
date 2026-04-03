from flask import Flask, render_template, jsonify
from tools.devcheck import *

app = Flask(__name__)


# time_sensor = Time(101, 'Фитнес-Хаус на Блюхера')
# temp_sensor = Temperature(201, 'Фитнес-Хаус на Блюхера')
# station = BusStation(6, 'Фитнес-Хаус на Блюхера', time_sensor, temp_sensor)
# bus = Bus('222', [station])

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
def show_status():
    global time_sensor, temp_sensor, station, bus

    station.connection()
    bus.connection()
    time_sensor.connection()
    temp_sensor.connection()

    return render_template('station_status.html', data=station.send_data(), bus=bus.send_GPS())


@app.route('/api/status')
def get_station_status():
    global station, bus

    station.update_info()
    bus.update_route_screen()

    return jsonify({
        'station': station.send_data(),
        'bus': bus.send_GPS()
    })


if __name__ == '__main__':
    time_sensor = Time(101, 'Фитнес-Хаус на Блюхера')
    temp_sensor = Temperature(201, 'Фитнес-Хаус на Блюхера')
    station = BusStation(6, 'Фитнес-Хаус на Блюхера', time_sensor, temp_sensor)
    bus = Bus('222', [station])

    app.run()
