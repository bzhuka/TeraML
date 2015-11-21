$(function(){
	$("#diagnosis_button").click(function(){
		$.ajax({
		url: 'http://localhost:8080/SpringMVC/diagnoseUser',
		type: 'POST',
                dataType: 'json',
                crossDomain: true,
                data: 
                	{"val" : $("#diagnosis_input").val()}
        ,
        success: function (json) {
        	$("#output").append(JSON.stringify(json))
        },            
        error: function (XMLHttpRequest, textStatus, errorThrown) {
        	alert("Was not able to process request : " + errorThrown);
        }
	});
	})
})