function display_record(activity){
    $("#activity_record").empty();
    let s = $("<tr><td>Time</td><td>Activity</td></tr>")
    $("#activity_record").append(s);
    for (let key in activity){
        let one = $("<tr><td>"+key+ "</td><td>"+activity[key]+"</td></tr>")
        $("#activity_record").append(one);
        // $("#activity_record").append("<br>");
    }

}
$(document).ready(function(){
    display_record(activity)
})
