const $ = require('jquery');

$(function () {
    $.getJSON('index.json', function (data) {
        $.each(data, function (i, f) {
            console.log(i);
        })
    })
})