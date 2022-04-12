function display_mostpop(mostpopular){
    $("#mostpop").empty();
    $.each(mostpopular, function(index,value){
        let newmovie = $("<div class = 'col-lg-3 lesspad'>");
        let content = $("<a href ='/view/"+ value.id + "'>" + "<img class = 'img-responsive fullwidth fullheight' src='"
        +value.image+ "'" + "alt= '"+value.title+"'></a>")
        newmovie.append(content)
        $("#mostpop").append(newmovie);
    })
    let viewmore = $("<div class = 'col-lg-3 lesspad'>");
    let content2 = $("<a href ='/view/all" + "'>" + "<img id = 'allbutton' class = 'img-responsive fullwidth fullheight' src='https://wallpaperaccess.com/full/217929.jpg' alt= 'view all'><span class = 'viewmore'> View More </span></a>")
    viewmore.append(content2)
    $("#mostpop").append(viewmore);
}

$(document).ready(function(){
    display_mostpop(mostpopular)   
})