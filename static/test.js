$(document).ready(function(){
    $('#nextbutton').prop('disabled', true);

    $( "#quiz_answer" ).submit(function( event ) {
        event.preventDefault();
        let str = $( "input" ).first().val()
        ans = $('input[name="choices"]:checked').val();
        console.log(ans);

        $('#nextbutton').prop('disabled', false);

        check_ans(ans);
      });

    $( "#give-up" ).click(function( event ) {
        $('#nextbutton').prop('disabled', false);
        ans = "give-up";
        console.log(ans);
        check_ans(ans);
    });
})

function check_ans(ans){
    ans_json = {
        "ans": ans,
        "num": one.id
    }

    console.log(ans_json)

    $.ajax({
        type: "POST",
        url: "/check_ans",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        // data : JSON.stringify(ans),
        data : JSON.stringify(ans_json),
        success: function(result){
            let feedback = result["feedback"]
            let correct = result["correct"]
            let real_ans = result["real_ans"]
            console.log(feedback)
            console.log(correct)
            console.log(real_ans)
            display_result(feedback, correct, real_ans);
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function display_result(feedback, correct, real_ans){
    if (correct === "True") {
        // let ans_text = $(`input[name="choices"][value=${real_ans}]`).prev('label').text();
        ans_text = one[real_ans]
        console.log(ans_text);
        $("#d_correct").text(`${ans_text} is correct!`)
    }
    else if (ans === "give-up"){
        ans_text = one[real_ans].toLowerCase()
        console.log(ans_text);
        $("#d_correct").text(`The correct answer is: ${ans_text}`)
    }
    else {
        ans_text = one[ans].toLowerCase()
        console.log(ans_text);
        $("#d_correct").text(`Sorry, but ${ans_text} is  incorrect`)
    }

    $("#d_feedback").text(feedback)
}
