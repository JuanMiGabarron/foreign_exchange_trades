$(document).ready(function(){
    $.getJSON( "/api/trades.json", function( data ) {
        var items = [];
        var item = '';
        $.each(data, function(key, val) {
            item = '<tr>';
            $.each(val, function(key, val) {
                item += ("<th>" + val + "</th>");
            });
            item += '</tr>';
            items.push(item);
        });
        $( "<tbody/>", {
            html: items.join("")
        }).appendTo("#trade_table");
    });
});