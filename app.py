from flask import Flask, render_template, jsonify, redirect, request
from tools.devcheck import *

app = Flask(__name__)


# time_sensor = Time(101, 'Фитнес-Хаус на Блюхера')
# temp_sensor = Temperature(201, 'Фитнес-Хаус на Блюхера')
# station = BusStation(6, 'Фитнес-Хаус на Блюхера', time_sensor, temp_sensor)
# bus = Bus('222', [station])

@app.route('/')
def connectionchecking():
    print('thingy')
    return redirect('/status')
    # time = Time(1, 'somewhere')
    # temp = Temperature(1, 'somewhere')
    # bs = BusStation(1, 'somewhere', time, temp)
    # bus = Bus('4', [bs])
    #
    # for creature in (time, temp, bs):
    #     print('\nChecking', type(creature))
    #     connection(creature)
    #     check_connection(creature)
    #     check_send_data(creature)
    #     check_request_data(creature)
    #     check_update_info(creature)
    #     if type(creature) is Temperature: check_temperature(creature)
    #     if type(creature) is BusStation: check_waitingtimes(creature)
    #
    # print('\nChecking', type(bus), '\n')
    # check_bus(bus)
    #
    # timec, tempc, bsc, busc = (time.check_connection(), temp.check_connection(),
    #                            bs.check_connection(), bus.check_connection())
    #
    # return render_template('connections.html', time=timec, temp=tempc, bs=bsc, bus=busc)


@app.route('/status')
def show_status():
    global time_sensor, temp_sensor, station, bus

    station.connection()
    bus.connection()
    time_sensor.connection()
    temp_sensor.connection()

    print('thingy')

    return render_template('station_status.html',
                           data=station.request_data(), bus=bus.request_data())


@app.route('/api/emulate')
def emulate_things():
    global station, bus

    station.update_info()
    bus.update_route_screen()

    return update_things()

@app.route('/api/update')
def update_things():
    global station, bus

    return jsonify({
        'station': station.request_data(),
        'bus': bus.request_data()
    })


@app.route('/api/push')
def push_things():
    global station, bus

    if request.args.get('type') == 'full':
        station.send_data(request)
        bus.send_GPS(request)
    elif request.args.get('type') == 'bus':
        bus.send_GPS(request)
    elif request.args.get('type') == 'busstation':
        station.send_data(request)
    return {}


if __name__ == '__main__':

    time_sensor = Time(101, 'Фитнес-Хаус на Блюхера')
    temp_sensor = Temperature(201, 'Фитнес-Хаус на Блюхера')
    station = BusStation(6, 'Фитнес-Хаус на Блюхера', time_sensor, temp_sensor)
    bus = Bus('222', [station])

    app.run()

