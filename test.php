<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Create a polyline using Geolocation and Google Maps API</title>
    <script src="https://maps.googleapis.com/maps/api/js?libraries=visualization&key=AIzaSyAGADiifvUELmMdOfy-UKlHPxNI6rrJUFE"></script>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
    <script>
      $(document).ready(function() {
        // If the browser supports the Geolocation API
        if (typeof navigator.geolocation == "undefined") {
          $("#error").text("Your browser doesn't support the Geolocation API");
          return;
        }
        // Save the positions' history
        var path = [];

        navigator.geolocation.watchPosition(function(position) {
          // Save the current position
          path.push(new google.maps.LatLng(position.coords.latitude, position.coords.longitude));

          // Create the map
          var myOptions = {
            zoom : 3,
            center : path[0],
            mapTypeId : google.maps.MapTypeId.ROADMAP
          }
          var map = new google.maps.Map(document.getElementById("map"), myOptions);

            path.push(new google.maps.LatLng(2.745537, 101.707316)); //mas
            path.push(new google.maps.LatLng(37.460353, 126.440674)); //kor
            path.push(new google.maps.LatLng(34.789594, 135.438084)); //jpn
            path.push(new google.maps.LatLng(-37.665357, 144.840642)); //aus
            path.push(new google.maps.LatLng(55.410343, 37.902312)); //rus
            path.push(new google.maps.LatLng(40.085148, 116.552407)); //chi
            path.push(new google.maps.LatLng(-6.127211, 106.653684)); //ind
            path.push(new google.maps.LatLng(1.364860, 103.991594)); //sin
            path.push(new google.maps.LatLng(40.760284, -73.772304)); //usa
            path.push(new google.maps.LatLng(53.358796, -2.272773)); //uk
            path.push(new google.maps.LatLng(40.498275, -3.567727)); //spa

          // Create the array that will be used to fit the view to the points range and
          // place the markers to the polyline's points
          var latLngBounds = new google.maps.LatLngBounds();
          for(var i = 0; i < path.length; i++) {
            latLngBounds.extend(path[i]);
            // Place the marker
            new google.maps.Marker({
              map: map,
              position: path[i],
              title: "Point " + (i + 1)
            });
          }
          var coordinates = [
            [
              //mas
              {lat:2.745537, lng:101.707316}, {lat:37.460353,lng:126.440674}, //to kor
              {lat:2.745537, lng:101.707316}, {lat:34.789594,lng:135.438084}, //to jpn
              {lat:2.745537, lng:101.707316}, {lat:40.085148,lng:116.552407}, //to chi
              {lat:2.745537, lng:101.707316}, {lat:-6.127211,lng:106.653684}, //to ind
              {lat:2.745537, lng:101.707316}, {lat:1.364860,lng:103.991594}, //to sin
              {lat:2.745537, lng:101.707316}, {lat:40.498275,lng:-3.567727}, //to spa
            ],[
              //kor
              {lat:37.460353, lng:126.440674}, {lat:34.789594,lng:135.438084}, //to jpn
              {lat:37.460353, lng:126.440674}, {lat:55.410343,lng:37.902312}, //to rus
              {lat:37.460353, lng:126.440674}, {lat:40.085148,lng:116.552407}, //to chi
            ],[
              //jpn
              {lat:34.789594,lng:135.438084}, {lat:55.410343,lng:37.902312}, //to rus
            ],[
              //aus
              {lat:-37.665357,lng:144.840642}, {lat:-6.127211,lng:106.653684}, //to ind
            ],[
              //rus
              {lat:55.410343,lng:37.902312}, {lat:40.085148,lng:116.552407}, //to chi
              {lat:55.410343,lng:37.902312}, {lat:53.358796,lng:-2.272773}, //to uk
              {lat:55.410343,lng:37.902312}, {lat:40.498275,lng:-3.567727}, //to spa
            ],[
              //chi
              {lat:40.085148,lng:116.552407}, {lat:53.358796,lng:-2.272773}, //to uk
              {lat:40.085148,lng:116.552407}, {lat:40.498275,lng:-3.567727}, //to spa
            ],[
              //ind
              {lat:-6.127211,lng:106.653684}, {lat:1.364860,lng:103.991594}, //to sin
            ],[
              //usa
              {lat:40.760284,lng:-73.772304}, {lat:53.358796,lng:-2.272773}, //to uk
              {lat:40.760284,lng:-73.772304}, {lat:40.498275,lng:-3.567727}, //to spa
            ],[  
              //uk
              {lat:53.358796,lng:-2.272773}, {lat:40.498275,lng:-3.567727}, //to spa
            ],
          ];

          // Creates the polyline object
          for(var i=0; i<coordinates.length; i++){
            var polyline = new google.maps.Polyline({
              map: map,
              path: coordinates[i],
              strokeColor: '#0000FF',
              strokeOpacity: 0.7,
              strokeWeight: 1,
              geodesic: true
            });
          }

          // Fit the bounds of the generated points
          map.fitBounds(latLngBounds);
          polyline.setMap(map);
        },
        function(positionError){
          $("#error").append("Error: " + positionError.message + "<br />");
        },
        {
          enableHighAccuracy: true,
          timeout: 10 * 1000 // 10 seconds
        });
      });
    </script>
    <style type="text/css">
      #map {
        width: 1250px;
        height: 600px;
        margin-top: 10px;
        margin-left: 50px;
      }
    </style>
  </head>
  <body>
    <h1>Create a polyline</h1>
    <div id="map"></div>
    <p id="error"></p>
    <div class="container">
      <form>
        <label for="origin">Origin</label>
        <select id="origin">
          <option value="mas">Malaysia - Kuala Lumpur (KUL)</option>
        </select>
        <br><br>
        <label for="dest">Destination</label>
        <select id="dest">
          <option value="kor">South Korea - Incheon (ICN)</option>
          <option value="jpn">Japan - Osaka (ITM)</option>
          <option value="aus">Australia - Melbourne (MEL)</option>
          <option value="rus">Russia - Moscow (SVO)</option>
          <option value="chi">China - Beijing (PEK)</option>
          <option value="ind">Indonesia - Jakarta (CGK)</option>
          <option value="sin">Singapore - Singapore (SIN)</option>
          <option value="usa">United States of America - John F. Kennedy (JFK)</option>
          <option value="uk">United Kingdoms - Manchester (MAN)</option>
          <option value="spa">Spain - Madrid (MAD)</option>
        </select>
      </form>
    </div>
  </body>
</html>