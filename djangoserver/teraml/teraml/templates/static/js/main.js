//Overall WS Access Variables
dbsAlias = 'HackSys'
wsHost = '153.64.73.150'
wsPort =  '1080'
path = '/tdrest/systems/' + dbsAlias + '/queries'
username = "hack_user12"
password = "tdhackathon"
$(function(){
	$("#PCA_button").click(function(){
                data = {"query" : 'select * from crime_data.murders_by_weapon_type'};
                alert(JSON.stringify(data));
		//--------this piece of code is to load into the mongodb once------
                $.ajax({
                        type: "POST",
                        url: "http://"+wsHost+":"+wsPort+path,
                        contentType: "application/json",
                        headers: {
                                'Accept': "application/vnd.com.teradata.rest-v1.0+json",
                                'Authorization': 'Basic ' + btoa(username + ':' + password)
                        },
                        data: JSON.stringify({
                                query: $("#PCA_input").val(),//"select * from crime_data.murders_by_weapon_type",
                                format: 'object'
                        }),
                        success: function (json) {
                                $("#PCA_output").append(JSON.stringify(json))
                        },            
                        error: function (XMLHttpRequest, textStatus, errorThrown) {
                                alert("Was not able to process request : " + errorThrown);
                        }
                });
                //----------
                //--------------This piece of code is to query the python backend---------
                /*$.ajax({
                        type: "GET",
                        url: "/query?val="+$("#PCA_input").val(),
                        contentType: "application/json",
                        data: {},
                        success: function (json) {
                                $("#PCA_output").append(JSON.stringify(json))
                        },            
                        error: function (XMLHttpRequest, textStatus, errorThrown) {
                                alert("Was not able to process request : " + errorThrown);
                        }
                })*/
        })
})
        