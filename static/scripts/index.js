let allowAutoUpdate = true
let updateInterval = setInterval(updateData, 2000)

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

function updateData() {
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
        }
    })
}

function manualUpdate() {
    updateData()
}