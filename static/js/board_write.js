Dropzone.autoDiscover = false;
var myDropzone;
var a;
$(function() {
	myDropzone = new Dropzone("#dropzone", {
		autoProcessQueue:false,
		uploadMultiple:true,
		parallelUploads:100,
		maxFiles:100,
		url: $("#dropzone").parents("form").attr("data-file-action")
	});

	$(".write-form").on("submit", function() {
		myDropzone.processQueue();
	});
	
	if($(".datepicker").length > 0) {
		$(".datepicker").datepicker({
			dateFormat:'yy-mm-dd',
			monthNamesShort: ['1','2','3','4','5','6','7','8','9','10','11','12'],
			monthNames: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'],
			dayNamesMin: ['일','월','화','수','목','금','토'],
			dayNames: ['일요일','월요일','화요일','수요일','목요일','금요일','토요일'],
			yearSuffix: "년"
		});
	}
});