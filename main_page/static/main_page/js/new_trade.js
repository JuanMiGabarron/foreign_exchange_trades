$(document).ready(function(){
    var rates = {};
    $(document).on('change', '#sell_currency', function() {
        $.getJSON(
            "http://api.fixer.io/latest?base=" + $(this).val(),
            function(data) {
            $.each(data['rates'], function(key, val) {
                rates[key] = val;
            });
            console.log(rates)
        });
    });

    $(document).on('change', '#buy_currency', buy_currency);

    var buy_currency = function(){
        console.log($('#buy_currency').val())
    };
});