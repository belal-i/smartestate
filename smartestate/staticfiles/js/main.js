import Cookies from './js.cookie.mjs';
$(document).ready(function() {
	if(Cookies.get("mode") == -1) {
		$(".navbar").toggleClass("navbar-dark");
		$(".navbar").toggleClass("bg-dark");
		$(".nav-item").toggleClass("text-dark");
		$(".listing-entry").toggleClass("bg-dark");
		$(".detail-images").toggleClass("bg-dark");
		$(".detail-short").toggleClass("bg-dark");
		$(".detail-long").toggleClass("bg-dark");
		$(".detail-text").toggleClass("text-dark");
		$(".back-to-listings").toggleClass("bg-dark");
		$("body").toggleClass("bg-dark");
		$("h2").toggleClass("text-dark");
		$("p").toggleClass("text-dark");
		$("span").toggleClass("text-dark");
		var dayNightIconPath = $("#toggle-day-night-icon").attr("src");
		dayNightIconPath = dayNightIconPath.replace("night", "day");
		$("#toggle-day-night-icon").attr("src", dayNightIconPath);
		$("#toggle-day-night-icon").css({"filter": "invert(100%)"});
	}
});
$("#toggle-day-night").click(function() {
	var mode;
	var dayNightIconPath = $("#toggle-day-night-icon").attr("src");
	if(Cookies.get("mode") == undefined) {
		mode = 1;
		Cookies.set("mode", mode, {sameSite: "strict"});
	} else {
		mode = Cookies.get("mode");
	}
	$(".navbar").toggleClass("navbar-dark");
	$(".navbar").toggleClass("bg-dark");
	$(".nav-item").toggleClass("text-dark");
	$(".listing-entry").toggleClass("bg-dark");
	$(".detail-images").toggleClass("bg-dark");
	$(".detail-short").toggleClass("bg-dark");
	$(".detail-long").toggleClass("bg-dark");
	$(".detail-text").toggleClass("text-dark");
	$(".back-to-listings").toggleClass("bg-dark");
	$("body").toggleClass("bg-dark");
	$("h2").toggleClass("text-dark");
	$("p").toggleClass("text-dark");
	$("span").toggleClass("text-dark");
	if(mode == 1) {
		dayNightIconPath = dayNightIconPath.replace("night", "day");
	} else {
		dayNightIconPath = dayNightIconPath.replace("day", "night");
	}
	$("#toggle-day-night-icon").attr("src", dayNightIconPath);
	if(mode == 1) {
		$("#toggle-day-night-icon").css({"filter": "invert(100%)"});
	} else {
		$("#toggle-day-night-icon").css({"filter": "none"});
	}
	mode *= -1;
	Cookies.set("mode", mode, {sameSite: "strict"});
});
