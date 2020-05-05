$("document").ready(function(){
    $("#send").click(function(){
        var message = $("#message").val();
        $.ajax({
            url: "http://localhost:5000/api/",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({"message": message})
        }).done(function(data) {
			document.getElementById('compiler').innerHTML=data['message'];
			console.log(data);
        });
    });
});