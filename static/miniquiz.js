var indices = ['a', 'b', 'c', 'd']

$(document).ready(function(){ 
    $('#nextbutton').hide()
    $("#test").hide()
    
    createQuestion()
    function createQuestion(){
        $.each(indices, function(i, v) {
            if (page_info.hasOwnProperty(v)){
                $('#rad').append(
                    $('<input>').prop({
                        type: 'radio',
                        id: v,
                        name: 'choices',
                        value: v,
                        class: 'testanswer'
                    })
                )
                // $('#rad').append(page_info[v])
                $('#rad').append(`<span id=text_${v}>${page_info[v]}</span>`)
                $('#rad').append(`<br>`)
            }
        })    

        
    }
    
    var inputElems = document.getElementsByClassName("testanswer");
    for (var i = inputElems.length - 1; i >= 0; --i) {
        var elem = inputElems[i];
        elem.onchange = function () {
            document.getElementById("submitonly").removeAttribute("disabled");
        };
    }
    
    $( "#quiz_answer" ).submit(function( event ) {
        event.preventDefault();
        ans = $('input[name="choices"]:checked').val();
        console.log(ans);
        $('#submitbuttons').hide();
        $('#nextbutton').show();
        $('#nextbutton').prop('disabled', false);

        display_result()
      });

    $( "#give-up" ).click(function( event ) {
        $('#nextbutton').prop('disabled', false);
        ans = "give-up";
        console.log(ans);
        $('#submitbuttons').hide();
        $('#nextbutton').show();
        
        display_result()
    });
})



function display_result(){
    // Always highlight the correct ans
    $(`#text_${page_info["answer"]}`).addClass("highlight_correct")
    console.log(`text_${page_info["answer"]}`)
    
    if (ans === page_info["answer"]) {
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
        // highlight incorrect ans
        $(`#text_${ans}`).addClass("highlight_wrong")
    }

    $("#d_feedback").text(page_info["feedback"])
    if (page_info.end == 0) {
        $("#test").remove()
    }
    else {
        $("#nextbutton").remove()
        $("#test").show()
    }
}
