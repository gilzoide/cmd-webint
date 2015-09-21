var textid;

$(function () {
	$('#submitModal').on('shown.bs.modal', function () {
    	$('#submitTitle')[0].focus()
  	});
	
    $('.text-row').on('click', function(event){
        textid = $(this).attr('data-textid');
        $.get( "/metrics/" + textid + ".html", function(data){
            $("#textInfoModalBody").html(data);
        });
    });

    $('#textInfoModal').on('shown.bs.modal', function () {
        $("#textInfoModalBody").scrollTop(0);
    });

    $('#submitTextButton').on('click', function () {
        $(this).prop('disabled', true);
        $(this).text("Submitting...");
        $('#submitForm').submit();
    });

    $('.submit-text-input').on('input', function () {
        var title = $('#submitTitle').val();
        var content = $('#submitContent').val();
        // TODO: add revised content.

        $('#submitTextButton').prop('disabled', title == '' ||
                                                content == '');
    });

    $('#exportCsvButton').on('click', function () {
        window.open("/metrics/" + textid + ".csv");
    });

    $('#exportArffButton').on('click', function () {
        window.open("/metrics/" + textid + ".arff");
    });

    $('#exportJsonButton').on('click', function () {
        window.open("/metrics/" + textid + ".pjson");
    });
});

function clearSubmitForm() {
    bootbox.confirm('This will <b>erase</b> everything you typed! Are you sure?',
                    function(result) {
                        if (result) {
                            $('#submitTextButton').prop('disabled', true);

                            $('#submitTitle').val('');
                            $('#submitAuthor').val('');
                            $('#submitSource').val('');
                            $('#submitDate').val('');
                            $('#submitGenre').val('');
                            $('#submitContent').val('');
                            $('#submitRevisedContent').val('');

                            setTimeout(function () {
                                $("#submitTitle").focus();
                            }, 1);
                        }
                    });
}
