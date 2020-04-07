
$(document).ready(function() {

    var $listMessage, $newQuest, $nb_post, $map;
    $listMessage = $('#list_message');
    $newQuest = $('#new_quest');
    $nb_post = 0;
    $map = '#map';

    $newQuest.on('submit', function(e){
        e.preventDefault();
        $listMessage.append('<div class="loader"></div>');
        $.ajax({
            data : {
                quest : $('#quest').val()
            },
            type : 'POST',
            url : '/quest'
        })
        .done(function(data){
            $( ".loader" ).remove();
            if (data.error == 1){
                $listMessage.append('<div class="message message_grandpy">' + data.message[0] + '</div>').fadeIn(1000);
            }else if (data.error == 0){
                $map = $map + $nb_post;
                $nb_post ++;
                $listMessage.append('<div class="message message_user">' + data.quest + '</div>').fadeIn(2000);
                $listMessage.append('<div class="message message_grandpy">' + data.message[0] + '</div>').fadeIn(2000);
                $listMessage.append('<div class="message reponse_grandpy">' + data.geo[0]['results'][0]['formatted_address'] + '</div>').fadeIn(3000);
                $coordinate = data.geo[0]['results'][0]['geometry']['location'];
                $listMessage.append('<div id="' + $map + '" class="map"></div>').fadeIn(5000);
                $($map).css("position","fixed !important");
                map = new google.maps.Map(document.getElementById($map), {
                    center: {lat: $coordinate['lat'], lng: $coordinate['lng']},
                    zoom: 8
                });
                $listMessage.append('<div class="message message_grandpy">' + data.message[1] + '</div>').fadeIn(6000);
                $listMessage.append('<div class="message reponse_grandpy">' + data.wiki + '</div>').fadeIn(7000);
        }})
    });
});