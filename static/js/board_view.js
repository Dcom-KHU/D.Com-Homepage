$(function() {
	$(".comment-reply-button").click(function(e) {
		e.preventDefault();
		$(".comment-reply", $(this).parents('.comment')).slideToggle();
	});
});