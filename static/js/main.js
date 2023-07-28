
'use strict';


$(window).on('load', function() {
	/*------------------
		Preloder
	--------------------*/
	$(".loader").fadeOut(); 
	$("#preloder").delay(400).fadeOut("fast");


	/*------------------
		Gallery item
	--------------------*/
	if($('.carbon-items-area').length > 0 ) {
		var containerEl = document.querySelector('.carbon-items-area');
		var mixer = mixitup(containerEl);
	}

});

(function($) {

	/*------------------
		Navigation
	--------------------*/
	$('.nav-switch').on('click', function(event) {
		$('.main-menu').slideToggle(400);
		event.preventDefault();
	});


	/*------------------
		Background Set
	--------------------*/
	$('.set-bg').each(function() {
		var bg = $(this).data('setbg');
		$(this).css('background-image', 'url(' + bg + ')');
	});


	/*------------------
		
	--------------------*/
    $('.rc-slider').owlCarousel({
		autoplay:true,
		loop: false,
		nav:true,
		dots: true,
		margin: 30,
		navText: ['', '<i class="fa fa-angle-right"></i>'],
		responsive:{
			0:{
				items:1
			},
			576:{
				items:2
			},
			990:{
				items:3
			},
			1200:{
				items:4
			}
		}
	});
    $('.profile-slider').owlCarousel({
		// autoplay:true,
		loop: true,
		// nav:true,
		// dots: true,
		startPosition:1,
		margin: 100,
		autowidth:true,
		navText: ['', '<i class="fa fa-angle-right"></i>'],
		responsive:{
			0:{
				items:3
			},
			576:{
				items:4
			},
			990:{
				items:6
			},
			1200:{
				items:8		
			}
		}
	});

    /*------------------
		Accordions
	--------------------*/
	$('.panel-link').on('click', function (e) {
		$('.panel-link').removeClass('active');
		var $this = $(this);
		if (!$this.hasClass('active')) {
			$this.addClass('active');
		}
		e.preventDefault();
	});




	$('.circle-progress').each(function() {
		var cpvalue = $(this).data("cpvalue");
		var cpcolor = $(this).data("cpcolor");
		var cptitle = $(this).data("cptitle");
		var cpid 	= $(this).data("cpid");
		var cpsize 	= $(this).data("cpsize");
		var cpbg 	= $(this).data("cpbg");

		$(this).append('<div class="'+ cpid +'"></div><div class="progress-info"><h2>'+ cpvalue +'%</h2><h4>'+ cptitle +'</h4></div>');

		if (cpvalue < 100) {

			$('.' + cpid).circleProgress({
				value: cpvalue/100 ,
				size: cpsize,
				thickness: 40,
				fill: cpcolor,
				emptyFill: cpbg
			});
		} else {
			$('.' + cpid).circleProgress({
				value: 1,
				size: cpsize,
				thickness: 40,
				fill: cpcolor,
				emptyFill: cpbg
			});
		}

	});

})(jQuery);

