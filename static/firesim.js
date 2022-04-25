//reference : https://www.elated.com/drag-and-drop-with-jquery-your-essential-guide/"

function makeFireMaterial(fire_material){
    $("#fire_materials").empty()
    $.each(fire_material, function(index,value){
        let name = value.name;
        let imagelink = value.image;
        let new_material = $("<div class = 'col-3 material'>")
        $(new_material).attr("order",value.ordernum)
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

function draggableMaterials(){
    $(".material").each(function(){
        $(this).draggable({"activeClass": "ui-state-highlight", "revert": "invalid"});
        $(this).hover(function(){
            $(this).css({"background-color":"lightyellow"});
            $(this).css("cursor","move"); 
            $(this).css("z-index",1000000); 
        },
        function(){
            $(this).css({"background-color":"white"});
            $(this).css("z-index",1)
        })
    })
}

function handleDrop( event, ui, order ) {
    var slotNumber = $(this).data( 'order' );
    if ( slotNumber == order ) {
        correct +=1;
        console.log(correct)
    } 
    if ( correct == 4 ) {
        $("#build").remove()
        $("#fire_materials").remove()
        $("#fire_answer").remove()
        $('#successMessage').show();
    } 
  }

$(document).ready(function(){ 
    $('#successMessage').hide();
    correct = 0;
    makeFireMaterial(fire_material);
    draggableMaterials();


    $('#fire1').droppable({ 
        accept: function(d) { 
            if(d.hasClass("material") && (d.attr('order') == '1' )){
                return true;
            }},
        classes:{
            "ui-droppable-active":"dark",
            "ui-droppable-hover":"darker"
        },
        drop :function(event,ui){
            order = ui.draggable[0].getAttribute("order")
            handleDrop(order);
        }
    }); 
    $('#fire2').droppable({ 
        accept: function(d) { 
            if(d.hasClass("material") && (d.attr('order') == '2' )){
                return true;
            }},
        classes:{
            "ui-droppable-active":"dark",
            "ui-droppable-hover":"darker"
        },
        drop :function(event,ui){
            order = ui.draggable[0].getAttribute("order")
            handleDrop(order);
        }
    }); 
    $('#fire3').droppable({ 
        accept: function(d) { 
            if(d.hasClass("material") && (d.attr('order') == '3' )){
                return true;
            }},
        classes:{
            "ui-droppable-active":"dark",
            "ui-droppable-hover":"darker"
        },
        drop :function(event,ui){
            order = ui.draggable[0].getAttribute("order")
            handleDrop(order);
        }
    }); 
    $('#fire4').droppable({ 
        accept: function(d) { 
            if(d.hasClass("material") && (d.attr('order') == '4' )){
                return true;
            }},
        classes:{
            "ui-droppable-active":"dark",
            "ui-droppable-hover":"darker"
        },
        drop :function(event,ui){
            order = ui.draggable[0].getAttribute("order")
            handleDrop(order);
        }
    }); 
})

