$(function() {
	$(".mobile-menu button").click(function() {
		$(".nav").toggleClass("active");
		$(".mobile-menu-mask").toggle();
	});

	$(".mobile-menu-mask").click(function() {
		$(".mobile-menu-mask").hide();
		$(".nav").removeClass("active");
	});
	
	if($(document).scrollTop() > $(".header").height()) {
		$(".header").addClass("header-fixed");
	}

	$(document).on("scroll", function() {
		if($(document).scrollTop() >= $(".header").height()) {
			$(".header").addClass("header-fixed");
		} else {
			$(".header").removeClass("header-fixed");
		}
	});

	if($(".banner ul li").length > 1)
		$(".banner ul").bxSlider();
});