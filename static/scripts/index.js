let allowAutoUpdate = true
let updateInterval = setInterval(updateData, 2000)

function updateStats(stats) {
    if (stats && stats.temperature) {
        document.getElementById('temp-avg').innerText = stats.temperature.avg + '°C';
        document.getElementById('temp-max').innerText = stats.temperature.max + '°C';
    } else {
        document.getElementById('temp-avg').innerText = '—';
        document.getElementById('temp-max').innerText = '—';
    }

    if (stats) {
        document.getElementById('bus-log-count').innerText = stats.bus_position_count || 0;
        if (stats.last_bus_position) {
            const pos = stats.last_bus_position;
            document.getElementById('bus-last-pos').innerText = 
                `Маршрут ${pos.route}: ${pos.lat}, ${pos.lon} (${pos.timestamp})`;
        } else {
            document.getElementById('bus-last-pos').innerText = '—';
        }
    } else {
        document.getElementById('bus-log-count').innerText = 0;
        document.getElementById('bus-last-pos').innerText = '—';
    }
}

function changeUpdateState() {
    allowAutoUpdate = !allowAutoUpdate
    console.log(allowAutoUpdate)

    if (allowAutoUpdate) {
        document.getElementById('btn-allowauto').innerHTML = "Отключить автообновление"
        updateData()
        updateInterval = setInterval(updateData, 2000)
    }
    else {
        document.getElementById('btn-allowauto').innerHTML = "Включить автообновление"
        clearInterval(updateInterval)
        updateInterval = null
    }
}

function emulateData() {
    $.ajax({
            type: 'GET',
            url: '/api/emulate',
            dataType: 'json',
            contentType: 'application/json',
            data: {},
            success: function (response) {
                if (response.station && response.station.sensors_data && response.station.sensors_data.clock) {
                    document.getElementById("clock-val").innerHTML = response.station.sensors_data.clock.value
                }

                if (response.station && response.station.sensors_data && response.station.sensors_data.temperature) {
                    document.getElementById("temp-val").innerHTML =
                        (response.station.sensors_data.temperature.value + '°C');
                }

                if (response.bus) {
                    document.getElementById('bus-coords').innerHTML =
                        (response.bus.lat + ', ' + response.bus.lon);
                }

                if (response.station && response.station.waiting_times) {
                    updateWaitingTable(response.station.waiting_times);
                }

                updateStats(response.stats);
            }
        })
}

function renewData() {
    $.ajax({
            type: 'GET',
            url: '/api/update',
            dataType: 'json',
            contentType: 'application/json',
            data: {},
            success: function (response) {
                if (response.station && response.station.sensors_data && response.station.sensors_data.clock) {
                    document.getElementById("clock-val").innerHTML = response.station.sensors_data.clock.value
                }

                if (response.station && response.station.sensors_data && response.station.sensors_data.temperature) {
                    document.getElementById("temp-val").innerHTML =
                        (response.station.sensors_data.temperature.value + '°C');
                }

                if (response.bus) {
                    document.getElementById('bus-coords').innerHTML =
                        (response.bus.lat + ', ' + response.bus.lon);
                }

                if (response.station && response.station.waiting_times) {
                    updateWaitingTable(response.station.waiting_times);
                }

                updateStats(response.stats);
            }
        })
}

function updateData() {
    if (allowAutoUpdate) emulateData()
    else renewData()
}

function manualUpdate() {
    updateData()
}

function sendData() {
    $.ajax({
        type: 'GET',
        url: '/api/push',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            'type': 'full',
            'clock': document.getElementById('clock-inp').value,
            'temp': document.getElementById('temp-inp').value,
            'lat': document.getElementById('bus-lat-inp').value,
            'lon': document.getElementById('bus-lon-inp').value,
        },
        success: function (response) { }
    })
    renewData()
    console.log(document.getElementById('clock-inp').value)
}

function sendBusData() {
    $.ajax({
        type: 'GET',
        url: '/api/push',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            'type': 'bus',
            'lat': document.getElementById('bus-lat-inp').value,
            'lon': document.getElementById('bus-lon-inp').value,
        },
        success: function (response) { }
    })
    renewData()
    console.log(document.getElementById('clock-inp').value)
}

function sendBusStationData() {
    $.ajax({
        type: 'GET',
        url: '/api/push',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            'type': 'busstation',
            'clock': document.getElementById('clock-inp').value,
            'temp': document.getElementById('temp-inp').value,
        },
        success: function (response) { }
    })
    renewData()
    console.log(document.getElementById('clock-inp').value)
}


function clearInputs() { document.querySelectorAll('input').forEach(input => input.value = '') }

function updateWaitingTable(waitingTimes) {
    const tbody = document.getElementById('waiting-table-body');

    if (!waitingTimes || Object.keys(waitingTimes).length === 0) {
        tbody.innerHTML = '<tr><td colspan="2" class="loading-text">Нет данных об автобусах</td></tr>';
        return;
    }

    let html = '';

    for (const [route, state] of Object.entries(waitingTimes)) {
        const statusText = state === 'near' ? 'Уже близко' : 'Еще едет';
        const statusClass = state === 'near' ? 'status-arriving' : 'status-waiting';

        html += `
            <tr>
                <td><strong>${route}</strong></td>
                <td><span class="${statusClass}">${statusText}</span></td>
            </tr>
        `;
    }

    tbody.innerHTML = html;
}