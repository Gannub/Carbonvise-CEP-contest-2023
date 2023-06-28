function initialize() {
	var myOptions = {
		zoom: 16,
		center: new google.maps.LatLng(13.73871335254652, 100.53253964497841), 
		mapTypeId: google.maps.MapTypeId.ROADMAP,
		scrollwheel: true,
		mapTypeControl: false,
		zoomControl: true,
		streetViewControl: false,
		}
	var map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);
	var marker = new google.maps.Marker({
		map: map,
		position: new google.maps.LatLng(13.73871335254652, 100.53253964497841) 
	});
	google.maps.event.addListener(marker, "click", function() {
		infowindow.open(map, marker);
	});
}
google.maps.event.addDomListener(window, 'load', initialize);


