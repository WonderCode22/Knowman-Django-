$(document).ready(function(){
    $(".tblescalation-detailview").on('click', function(){
        event.preventDefault();
        var url_to = $(this).attr("href");
        var send_data = $(this).text();
        $.ajax({
            type: "POST",
            url: "1/",
            dataType: "json",
            data: {
                case_id: send_data,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(return_value){
                html = "";
                for(key in return_value)
                {
                    html += "<div class='terms'><h2>" + key.charAt(0).toUpperCase() + key.slice(1) + "</h2>";
                    html += "<h3>"+ return_value[key] +"</h3>";
                    html += "</div>"
                }
                $("#detail-view").html(html);
            }
        })
    })
});
