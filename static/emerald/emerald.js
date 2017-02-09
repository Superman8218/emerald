$(document).ready( function() {

	//Determine which of the tabs should be highlighted

	var url = window.location.pathname;
	var domain = "home";
	if (url.length > 1) // If we are at the home page, the url will be "/"
	{
		var url_split = url.split("/");
		domain = url_split[1];
	}
	$("."+domain).addClass("active");


	$(".nav a").on("click", function(){
   		$(".nav").find(".active").removeClass("active");
   		$(this).parent().addClass("active");
	});

});

