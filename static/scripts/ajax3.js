setInterval(updateData, 1000)

function updateData() {
    $.ajax({
        type: 'GET',
        url: '/api/status',
        dataType: 'json',
        contentType: 'application/json',
        data: {},
        success: function (response) {
            if (response.station && response.station.sensors_data && response.station.sensors_data.clock) {
                $('#clock-val').text(response.station.sensors_data.clock.value);
            }

            // Обновляем температуру на остановке
            if (response.station && response.station.sensors_data && response.station.sensors_data.temperature) {
                $('#temp-val').text(response.station.sensors_data.temperature.value + '°C');
            }

            // Обновляем координаты автобуса
            if (response.bus) {
                $('#bus-coords').text(response.bus.lat + ', ' + response.bus.lon);
        }
    }})
}