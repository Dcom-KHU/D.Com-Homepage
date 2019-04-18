$(function() {
	processing_latest_notice_list = false;

	function slide_notice_left() {
		if(processing_latest_notice_list) return;
		
		var $element = $(".latest-notice-list ul");
		var item_width = $("li", $element).width() + 30;
		var current_scroll = $element.scrollLeft();

		if(current_scroll <= 0)
			return;

		var to_scroll = Math.max(current_scroll - item_width, 0);

		processing_latest_notice_list = true;
		$element.animate({scrollLeft:to_scroll}, 300, function() {
			processing_latest_notice_list = false;
		});
	}

	function slide_notice_right() {
		if(processing_latest_notice_list) return;
		
		var $element = $(".latest-notice-list ul");
		var item_width = $("li", $element).width() + 30;
		var current_scroll = $element.scrollLeft();

		var to_scroll = current_scroll + item_width;

		processing_latest_notice_list = true;
		$element.animate({scrollLeft:to_scroll}, 300, function() {
			processing_latest_notice_list = false;
		});
	}

	$(".latest-notice .slide-left button").click(slide_notice_left);
	$(".latest-notice .slide-right button").click(slide_notice_right);
	$(".latest-notice-list ul").swipe({
		swipeLeft:slide_notice_right,
		swipeRight:slide_notice_left
    });
});