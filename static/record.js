function display_record(activity){
    $("#activity_record").empty();
    for (let key in activity){
        let one= $("<div>"+key+"    "+activity[key]+"</div>")
        $("#activity_record").append(one);
        $("#activity_record").append("<br>");
    }

}

$(document).ready(function(){
    display_record(activity)
})