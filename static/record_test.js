function display_record_test(test_record){
    $("#test_record").empty();
    let s = $("<tr><td>Tests</td><td>Results</td></tr>")
    $("#test_record").append(s);
    for (let key in test_record){
        let one = $("<tr><td>"+"Attempt  "+key+ "</td><td>"+test_record[key]+"</td></tr>")
        $("#test_record").append(one);
        // $("#activity_record").append("<br>");
    }

}
$(document).ready(function(){
    display_record_test(test_record)
})