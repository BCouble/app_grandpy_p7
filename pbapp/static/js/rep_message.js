/*class Message {
    constructor(name, id, message) {
        this.name = name;
        this.id = id;
        this.message = message;
    }

}

let myMessage = new Message("Papy", "01", "Hello");
console.log(myMessage)
$.ajax({
	data : {
		question: $('#question').val()
	},
	type : 'POST',
	url : '/quest'
})*/
/*
$(function() {
    $.ajax({
        type : 'POST',
	    url : '/quest',
	    success: function(data) { console.log("hello world !");
    });
};
};
    $.ajax({
        url: "/quest",
        type : "POST",
        data: {
            param1 : "value1",
            param2 : "value2"
        }
    })
    .done (function(data) {

     })
    .fail (function()  { alert("Error ")   ; })
    ;

*/
/*
$(document).ready(function() {

    var $listMessage, $newQuest;
    $listMessage = $('list_message');
    $newQuest = $('#new_quest');

    $newQuest.on('submit', function(e){
        e.preventDefault();
        $.ajax({
            data: {
                quest = $('input:text').val();
            },
            type:'POST',
            url: '/quest'
        })
        .done(function(data){
            alert(data);
        })
        $listMessage.append('<li>' +data+ '</li>');
    });

});
*/
$(function(){

    var $listMessage, $newQuest;
    $listMessage = $('list_message');
    $newQuest = $('#new_quest');

    $newQuest.on('submit', function(e){
        e.preventDefault();
        $.ajax({
            data : {
                quest : $('#quest').val()
            },
            type : 'POST',
            url : '/quest'
        });
    });
});