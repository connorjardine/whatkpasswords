var codes_array = [];
var iter = 0;

$("button").click(function() {
    codes_array.push(this.value);
    iter += 1;
    console.log(codes_array);
    if( iter >= 3) {
        console.log(iter);
        $.ajax({
            url: $SCRIPT_ROOT + '/submit_login',
            type: "POST",
            data: {
                code_zero: codes_array[0],
                code_one: codes_array[1],
                code_two: codes_array[2]
            },
            success: function (result) {
                if (result === "True") {
                    window.location.href = '/authenticated/auth';
                }
                else {
                    iter = 0;
                    codes_array = [];
                    $("#incorrectPassword").css({"display": "inline-block"});
                    setTimeout(function() {
                        $("#incorrectPassword").css({"display": "none"});
                    }, 1000);
                }
            }
        });
    }
});