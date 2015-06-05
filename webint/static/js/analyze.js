$(function () {
	$('#submitModal').on('shown.bs.modal', function () {
    	$('#submitTitle').focus()
  	});
	
    $('.text-row').on('click', function(event){
        var textid = $(this).attr('data-textid');
        $.get( "/metrics/" + textid, function(data){
            $( "#textInfoModalBody").html(data);
        });
    });
});
