from flask import Flask, render_template
from Sensors import *
from BusStation import *
from devcheck import *

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



if __name__ == '__main__':
    app.run()