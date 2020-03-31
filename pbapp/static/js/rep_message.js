$(function(){

    var $listMessage, $newQuest;
    $listMessage = $('#list_message');
    $newQuest = $('#new_quest');

    $newQuest.on('submit', function(e){
        e.preventDefault();
        $.ajax({
            data : {
                quest : $('#quest').val()
            },
            type : 'POST',
            url : '/quest'
        })
        .done(function(data){
            $listMessage.append('<div class="message message_user">' + data.quest + '</div>');
            $listMessage.append('<div class="message message_grandpy">' + data.geo[0]['results'][0]['formatted_address'] + '</div>');
            $coordinate = data.geo[0]['results'][0]['geometry']['location'];
            $listMessage.append('<div id="map"></div>');
            $("#map").css("position","fixed !important");
            map = new google.maps.Map(document.getElementById('map'), {
                center: {lat: $coordinate['lat'], lng: $coordinate['lng']},
                zoom: 8
            });
            $listMessage.append('<div class="message message_grandpy">' + data.wiki + '</div>');
        })
    });
});