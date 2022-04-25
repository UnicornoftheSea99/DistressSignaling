var indices = ['a', 'b', 'c', 'd']

$(document).ready(function(){ 
        // for (var key, value of one)
        // {
        $.each(indices, function(i, v) {
            if (page_info.hasOwnProperty(v)){
                $('#rad').append(
                    $('<input>').prop({
                        type: 'radio',
                        id: v,
                        name: 'choices',
                        value: v
                    })
                )

                $('#rad').append(page_info[v])
                $('#rad').append(`<br>`)
            }
        })

    $('#nextbutton').prop('disabled', true);

    $( "#quiz_answer" ).submit(function( event ) {
        event.preventDefault();
        ans = $('input[name="choices"]:checked').val();
        console.log(ans);

        $('#nextbutton').prop('disabled', false);

        display_result()
      });

    $( "#give-up" ).click(function( event ) {
        $('#nextbutton').prop('disabled', false);
        ans = "give-up";
        console.log(ans);
        display_result()
    });
})



function display_result(){
    
    if (ans === page_info["answer"]) {
        // let ans_text = $(`input[name="choices"][value=${real_ans}]`).prev('label').text();
        ans_text = page_info[ans]
        console.log(ans_text);
        $("#d_correct").text(`${ans_text} is correct!`)
    }
    else if (ans === "give-up"){
        ans_text = page_info[page_info.answer].toLowerCase()
        console.log(ans_text);
        $("#d_correct").text(`The correct answer is: ${ans_text}`)
    }
    else {
        ans_text = page_info[ans].toLowerCase()
        console.log(ans_text);
        $("#d_correct").text(`Sorry, but ${ans_text} is  incorrect`)
    }

    $("#d_feedback").text(page_info["feedback"])
}
