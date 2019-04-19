function validate(f) {
	if(!$("#agree").is(":checked")) {
		alert("회원가입약관에 동의하셔야 가입하실 수 있습니다.");
		return false;
	}
	if(!$("#agree2").is(":checked")) {
		alert("개인정보취급방침에 동의하셔야 가입하실 수 있습니다.");
		return false;
	}
}

$(function() {
	$("#all-agree").click(function() {
		var checked = $("#all-agree").is(":checked");

		$("#agree").prop("checked", checked);
		$("#agree2").prop("checked", checked);
		$("#agree").attr("checked", checked);
		$("#agree2").attr("checked", checked);
	});
});