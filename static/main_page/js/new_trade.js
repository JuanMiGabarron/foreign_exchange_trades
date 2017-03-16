$(document).ready(function(){
    var rates = {};                                                         //var which we use to store the current rates
    var buy_ccy;                                                            //var to store the current buy currency
    var current_rate;                                                       //var to store the current rate
    var sell_amount;                                                        //var to store the amount of money to sell

    var clear_vars = function(){                                            //function to clear all the variables
        rates = {};
        buy_ccy = null;
        current_rate = null;
        sell_amount = null;
    };

    var clear_form = function(){                                            //funtion to clear all the data fields after post them by api
        $('#sell_currency').val('')
        $('#sell_amount').val('')
        $('#buy_currency').val('')
        $('#buy_amount').val('')
        $('#current_rate').text('');
    };

    var can_trade = function(val){                                          //function to update the create trade button to control invalid data
        $('#create_trade').prop('disabled', !val);
    };

    var update_amount = function(){                                         //function used to update buy amount if sell amount is a valid number
        if(current_rate){
            sell_amount = +$('#sell_amount').val();                         //use "+" before the val to cast the string to a number
            if(sell_amount > 0){
                can_trade(true);
            }else{
                can_trade(false);
            }
            $('#buy_amount').val((sell_amount*current_rate).toFixed(2));    //calculate buy amount and fix the decimal to 2 with toFixed(2)
        }else{
            $('#buy_amount').val('');
            can_trade(false);
        }
    };

    var buy_currency = function(){                                          //function to update the rate based on the selected buy currency
        buy_ccy = $('#buy_currency').val();
        current_rate = rates[buy_ccy];
        if(buy_ccy){
            if(current_rate){
                $('#current_rate').text(current_rate);
            }else{
                $('#current_rate').text('');                                //if current rate doesn't exit this means buy currency and sell currency are equals so, a warning appears
                $('.alert-warning').show();
            }
        }
        update_amount();                                                    //Call update amount to update the buy amount because maybe the rates have changed
    };

    var trade_success = function(){                                         //function called after trade creation and post it by api, here we display success alert and clear vars and fields
        can_trade(false);
        clear_vars();
        clear_form();
        $('.alert-success').show();
    };

    $(document).on('change', '#sell_currency', function() {                 //function to call fixer.io api when we choose a sell currency
        $.getJSON(
            "http://api.fixer.io/latest?base=" + $(this).val(),
            function(data) {
                rates = {};
                $.each(data['rates'], function(ccy, rate) {                 //here the rates are updated with the new rates and currencies
                    rates[ccy] = rate;
            });
            buy_currency();                                                 //we make this call because we need to update the current rate and buy amount
        });
    });

    $(document).on('change', '#buy_currency', buy_currency);                //if the select of buy currency change call buy_currency

    $(document).on('keyup', '#sell_amount', update_amount);                 //every time we press a key in the sell amount, we update the buy amount

    $(document).on('click', '#create_trade', function(){                    //function called when create button is clicked
        var data = '{\
                        "sell_currency":"' + $('#sell_currency').val() + '",\
                        "sell_amount": ' + sell_amount.toFixed(2) + ',\
                        "buy_currency":"' + buy_ccy + '",\
                        "buy_amount": ' + $('#buy_amount').val() + ',\
                        "rate":' + current_rate + '\
                    }';
        $.ajax({                                                            //Use ajax to post the json data throw the API
            type: "POST",
            url: '/api/trades/',
            data: data,
            success: trade_success,                                         //if the post is success, we call trade success
            contentType: 'application/json',
            dataType: 'json'
        });
    });

    $(document).on('mouseenter', '.alert-success, .alert-warning', function(){
        $(this).hide();                                                     //function to hide the success and warning alerts if the mouse enter into them
    });
});