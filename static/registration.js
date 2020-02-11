var codes_array = [];
var first_input = [];
var iter = 0;

$("button").click(function() {
    codes_array.push(this.value);
    iter += 1;
    console.log(codes_array);
    if( iter === 3) {
        console.log(iter);
        if(first_input === undefined || first_input.length === 0) {
            first_input = codes_array;
            codes_array = [];
            iter = 0;
        }
        else{
            console.log(codes_array.toString());
            console.log(first_input.toString());
            if(codes_array.toString() === first_input.toString()) {
                $.ajax({
                    url: $SCRIPT_ROOT + '/submit_registration',
                    type: "POST",
                    data: {
                        code_zero: codes_array[0],
                        code_one: codes_array[1],
                        code_two: codes_array[2]
                    },
                    success: function (result) {
                        console.log(result);
                            window.location.href = result;
                    }
                });
            }
            else{
                console.log("show error message and clear variables to start again.");
                iter = 0;
                codes_array = [];
                first_input = [];
            }
        }
    }
});