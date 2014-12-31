$(function () {
	$('.text-row').on('click', function () {
		window.alert('clicked');
	});

	$('#submitModal').on('shown.bs.modal', function () {
    	$('#submitTitle').focus()
  	});
});