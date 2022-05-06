$("#toggle-day-night").click(function() {
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
});
