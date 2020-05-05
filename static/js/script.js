$("document").ready(function(){
    $("#send").click(function(){
        var message = $("#message").val();
        $.ajax({
            url: "http://localhost:5000/api",
            type: "POST",
            dataType:"json",
            data: {"message": message},
            success: function(data){
                document.getElementById('compiler').innerHTML=data['message'];
                console.log(data);
            }
        });
    });
});
