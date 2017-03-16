$(document).ready(function(){
    $.getJSON( "/api/trades.json", function(data) {                     //Call to the API, we get a json
        var trades = [];                                                //var to store all the trades
        var trade = '';                                                 //var to store the current html of a trade
        var date;
        $.each(data, function(pos, obj) {                               //we walk throw the json
            trade = '<tr>';
            $.each(obj, function(key, val) {                            //we walk throw the trade object
                if(key=='date_booked'){
                    date = $.format.date(val, "yyyy/MM/dd HH:mm:ss");   //we use jquery-dateFormat plugging to format the date, to avoid overload the api
                    trade += ("<th>" + date + "</th>");
                }else if(key=="rate"){
                    trade += ("<th>" + parseFloat(val) + "</th>");      //use parseFloat to remove unnecessaries 0's
                }else{
                    trade += ("<th>" + val + "</th>");
                }
            });
            trade += '</tr>';
            trades.push(trade);                                         //save the current trade
        });
        $( "<tbody/>", {
            html: trades.join("")
        }).appendTo("#trade_table");                                    //append the html to the end of trade_table node
    });
});