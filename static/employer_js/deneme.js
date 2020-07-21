$('#country').change(function() {
    var country = $('#country').val();
    find_cities(cities)



    // var listtt = {{ cities }};
    // var listt = JSON.parse(cities);
    // find_cities(country)
});

function find_cities(cities) {
    var parsed = JSON.parse('{{cities | tojson}}');

    var json_data = {
        "aaa" : JSON.stringify(cities)
    };
}