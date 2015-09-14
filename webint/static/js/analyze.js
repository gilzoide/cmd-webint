$(function () {
	$('#submitModal').on('shown.bs.modal', function () {
    	$('#submitTitle')[0].focus()
  	});
	
    $('.text-row').on('click', function(event){
        var textid = $(this).attr('data-textid');
        $.get( "/metrics/" + textid + ".html", function(data){
            $("#textInfoModalBody").html(data);
        });
    });

    $('#textInfoModal').on('shown.bs.modal', function () {
        $("#textInfoModalBody").scrollTop(0);
    });
});

function clearSubmitForm() {
    bootbox.confirm('This will <b>erase</b> everything you typed! Are you sure?',
                    function(result) {
                        if (result) {
                            $('#submitTitle')[0].value = "";
                            $('#submitAuthor')[0].value = "";
                            $('#submitSource')[0].value = "";
                            $('#submitDate')[0].value = "";
                            $('#submitGenre')[0].value = "";
                            $('#submitContent')[0].value = "";

                            // $('#submitTitle')[0].focus();
                        }
                    });
}
