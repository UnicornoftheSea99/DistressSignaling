
$(document).ready(function(){
    $( "#search").submit(function( event ) {
      event.preventDefault();
      console.log("Whitespace")
      if ($("#searchval").val().trim().length == 0){
        $("#searchval").val('')
        $("#searchval").focus()
      }
      else{
        var url = "/search/" + $("#searchval").val()
        console.log(url)   
        location.href = url
      }
    });
})
