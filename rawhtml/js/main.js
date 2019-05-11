$(function() {
	processing_latest_gallery_list = false;

	function slide_gallery_left() {
		if(processing_latest_gallery_list) return;
		
		var $element = $(".latest-gallery-list ul");
		var item_width = $("li", $element).width() + 30;
		var current_scroll = $element.scrollLeft();

		if(current_scroll <= 0)
			return;

		var to_scroll = Math.max(current_scroll - item_width, 0);

		processing_latest_gallery_list = true;
		$element.animate({scrollLeft:to_scroll}, 300, function() {
			processing_latest_gallery_list = false;
		});
	}

	function slide_gallery_right() {
		if(processing_latest_gallery_list) return;
		
		var $element = $(".latest-gallery-list ul");
		var item_width = $("li", $element).width() + 30;
		var current_scroll = $element.scrollLeft();

		var to_scroll = current_scroll + item_width;

		processing_latest_gallery_list = true;
		$element.animate({scrollLeft:to_scroll}, 300, function() {
			processing_latest_gallery_list = false;
		});
	}

	$(".latest-gallery .slide-left button").click(slide_gallery_left);
	$(".latest-gallery .slide-right button").click(slide_gallery_right);
	$(".latest-gallery-list ul").swipe({
		swipeLeft:slide_gallery_right,
		swipeRight:slide_gallery_left
    });
});