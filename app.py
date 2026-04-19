from flask import Flask, render_template, jsonify, redirect, request
from models.Bus import Bus
from models.BusStation import BusStation
from models.Sensors import Temperature, Time

app = Flask(__name__)

@app.route('/')
def connectionchecking():
    print('thingy')
    return redirect('/status')


@app.route('/status')
def show_status():
    global time_sensor, temp_sensor, station, bus

    station.connection()
    bus.connection()
    time_sensor.connection()
    temp_sensor.connection()

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
    station = BusStation(6, 'Фитнес-Хаус на Блюхера', (59.978165, 30.373342), time_sensor, temp_sensor)
    bus = Bus('222', [station], (59.9343, 30.3351))
    station.add_bus(bus)

    app.run()
