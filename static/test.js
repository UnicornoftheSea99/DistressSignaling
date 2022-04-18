$(document).ready(function(){
    $('#nextbutton').prop('disabled', true);

    $( "#quiz_answer" ).submit(function( event ) {
        event.preventDefault();
        let str = $( "input" ).first().val()
        ans = $('input[name="1"]:checked').val();
        console.log(ans);

        $('#nextbutton').prop('disabled', false);

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
            console.log(feedback)
            console.log(correct)
            display_result(feedback, correct);
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function display_result(feedback, correct){
    if (correct === "True")
        $("#d_correct").text("Correct!")
    else
        $("#d_correct").text("Sorry, but that's incorrect")

    $("#d_feedback").text(feedback)
}