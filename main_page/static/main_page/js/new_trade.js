$(document).ready(function(){
    var rates = {};
    var buy_ccy;
    var current_rate;
    var sell_amount;

    var clear_vars = function(){
        rates = {};
        buy_ccy = null;
        current_rate = null;
        sell_amount = null;
    };

    var clear_form = function(){
        $('#sell_currency').val('')
        $('#sell_amount').val('')
        $('#buy_currency').val('')
        $('#buy_amount').val('')
        $('#current_rate').text('');
    };

    var can_trade = function(val){
        $('#create_trade').prop('disabled', !val);
    };

    var update_amount = function(){
        if(current_rate){
            sell_amount = +$('#sell_amount').val();
            console.log(sell_amount)
            if(sell_amount > 0){
                can_trade(true);
            }else{
                can_trade(false);
            }
            $('#buy_amount').val((sell_amount*current_rate).toFixed(2));
        }else{
            $('#buy_amount').val('');
            can_trade(false);
        }
    };

    var buy_currency = function(){
        buy_ccy = $('#buy_currency').val();
        current_rate = rates[buy_ccy];
        if(buy_ccy){
            if(current_rate){
                $('#current_rate').text(current_rate);
            }else{
                $('#current_rate').text('');
                //some tipe of warning
            }
        }
        update_amount();
    };

    var trade_success = function(){
        can_trade(false);
        clear_vars();
        clear_form();
        $('.alert-success').show();
    };

    $(document).on('change', '#sell_currency', function() {
        $.getJSON(
            "http://api.fixer.io/latest?base=" + $(this).val(),
            function(data) {
                rates = {};
                $.each(data['rates'], function(key, val) {
                    rates[key] = val;
            });
            buy_currency();
        });
    });

    $(document).on('change', '#buy_currency', buy_currency);
    $(document).on('keyup', '#sell_amount', update_amount);

    $(document).on('click', '#create_trade', function(){
        var data = '{\
                        "sell_currency":"' + $('#sell_currency').val() + '",\
                        "sell_amount": ' + sell_amount.toFixed(2) + ',\
                        "buy_currency":"' + buy_ccy + '",\
                        "buy_amount": ' + $('#buy_amount').val() + ',\
                        "rate":' + current_rate + '\
                    }';
        console.log(data)
        $.ajax({
            type: "POST",
            url: '/api/trades/',
            data: data,
            success: trade_success,
            contentType: 'application/json',
            dataType: 'json'
        });
    });
    $(document).on('mouseenter', '.alert-success', function(){
        $(this).hide();
    });
});