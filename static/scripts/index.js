setInterval(updateData, 3000)

function updateData() {
    $.ajax({
        type: 'GET',
        url: '/api/status',
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