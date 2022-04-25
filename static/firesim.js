function makeFireMaterial(fire_material){
    $("#fire_materials").empty()
    $.each(fire_material, function(index,value){
        let name = value.name;
        let imagelink = value.image;
        let new_material = $("<div class = 'col-3'>")
        let namerow = $("<div class = 'row'>")
        let imagerow = $("<div class = 'row imagerow'>")
        let image = $("<img class = 'img-fluid'>")
        $(namerow).text(name)
        $(image).attr("src",imagelink)
        $(image).attr("alt",name)
        $(imagerow).append(image)
        $(new_material).append(namerow)
        $(new_material).append(imagerow)
    $("#fire_materials").prepend(new_material)
    });
}

$(document).ready(function(){ 
    makeFireMaterial(fire_material)
})
