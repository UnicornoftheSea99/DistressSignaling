function display_info(page_info){
    $("#infoblock1").empty();
    $("#infoblock2").empty();
    $("#infoblock3").empty();
    $("#media").empty();
    let ib1 = page_info.info1;
    let ib2 = page_info.info2;
    let ib3 = page_info.info3;
    let media = page_info.media;
    //info block 1
    if (ib1[0] != ""){
        let h1= $("<div class = 'row header accentcolor'>")
        $(h1).text(ib1[0])
        $("#infoblock1").append(h1);
    }
    let info1= $("<div><ul>")
    if (Array.isArray(ib1[1])){
        for (item in ib1[1]){
            let new_listitem = $("<li>" + ib1[1][item] + "</li>")
            $(info1).append(new_listitem);
        }
        $(info1).append("</ul>");
        $("#infoblock1").append(info1);

    }
    else{
        $(info1).text(ib1[1])
        $("#infoblock1").append(info1);
    }
    //info block 2
    if (ib1[0] != ""){
        let h2= $("<div class = 'row header accentcolor'>")
        $(h2).text(ib2[0])
        $("#infoblock2").append(h2);
    }
    let info2= $("<div>")
    if (Array.isArray(ib2[1])){
        $(info2).append("<ul>");
        for (item in ib2[1]){
            let new_listitem = $("<li>" + ib2[1][item] + "</li>")
            $(info2).append(new_listitem);
            $(info2).append("<br>");
        }
        $(info2).append("</ul>");
        $("#infoblock2").append(info2);
    }
    else{
        $(info2).text(ib2[1])
        $("#infoblock2").append(info2);
    }
    //info block 3
    if (ib1[0] != ""){
        let h3= $("<div class = 'row header accentcolor'>")
        $(h3).text(ib3[0])
        $("#infoblock3").append(h3);
    }
    let info3 = $("<div style='color: darkgrey '>")
    if (Array.isArray(ib3[1])){
        $(info3).append("<ul>");
        for (item in ib3[1]){
            let new_listitem = $("<li>" + ib3[1][item] + "</li>")
            $(info3).append(new_listitem);
            $(info3).append("<br>");
        }
        $(info3).append("</ul>");
        $("#infoblock3").append(info3);
    }
    else{
        $(info3).text(ib3[1])
        $("#infoblock3").append(info3);
    }
    //media
    let imagerow = $("<div class = 'row'>")
    for (image in media){
        let imagecol= $("<div class = 'col'>")
        let new_image = $("<img class = 'learnimg'>")
        $(new_image).attr("src",media[image])
        $(new_image).attr("alt",page_info.page_title)
        $(imagerow).append(imagecol)
        $(imagecol).append(new_image)
    }

    $("#media").append(imagerow);
    if (page_info.end == 0) {
        $("#test").remove()
    }
    else {
        $("#nextbutton").remove()
    }
}

$(document).ready(function(){
    display_info(page_info)
})
