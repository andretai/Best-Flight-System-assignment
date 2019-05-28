<?php
if (isset($_POST['search'])) {
    $from = $_POST['origin'];
    $to = $_POST['dest'];
}
?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Best Flight</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>      
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
        height: 550px;
        left: 60px;
        right: 50px;
        top: 10px;
        bottom: 0px;
        position:relative;
      }
    </style>
  </head>
  <body>
    <h1 align="center">FSK Flight Recommendation System</h1>
    <div id="map"></div>
    <p id="error"></p>
    <div class="container" align="center">
      <form action="<?php echo $_SERVER['PHP_SELF'] ?>" method="post">
        <label for="origin">Origin</label>
        <br>
        <select id="origin" name="origin">
          <option value="A">Malaysia - Kuala Lumpur (KUL)</option>
        </select>
        <br><br>
        <label for="dest">Destination</label>
        <br>
        <select id="dest" name="dest">
          <option value="B">South Korea - Incheon (ICN)</option>
          <option value="C">Japan - Osaka (ITM)</option>
          <option value="D">Australia - Melbourne (MEL)</option>
          <option value="E">Russia - Moscow (SVO)</option>
          <option value="F">China - Beijing (PEK)</option>
          <option value="G">Indonesia - Jakarta (CGK)</option>
          <option value="H">Singapore - Singapore (SIN)</option>
          <option value="I">United States of America - New York (JFK)</option>
          <option value="J">United Kingdoms - Manchester (MAN)</option>
          <option value="K">Spain - Madrid (MAD)</option>
        </select>
        <br><br>
        <button type="submit" name="search">Search</button>
      </form>
      <br>
      <table>
        <tr>
          <th>No.</th>
          <th>Pathway</th>
        </tr>
        <tr>
          <th>1</th>
          <th id="result"></th>
        </tr>
      </table>
      <script>
        var graph = [
            'AK11098','AF3200','AB4601','AC4975',
            'AG1125','AH297','KF9227','KE3444',
            'KJ1432','KI5775','FE5000','FJ8115',
            'FB903','BE6598','BC862','CE7344',
            'GD5204','GH9879','EJ2585','JI5376'
        ];
        
        var parseEdge = (edge) => {
            var [left, right, ...cost] = edge;
            cost = parseInt(cost.join(''), 10);
            return { left, right, cost };
        };
        
        var addToMap = (map, origin, vertex, cost) => {
            (map[origin] = map[origin] || [])
            .push({ vertex, cost });
        };
        
        var graphToMap = (graph) => {
            var map = {};
        
            for (var edge of graph) {
            var { left, right, cost } = parseEdge(edge);
        
            addToMap(map, left, right, cost);
            addToMap(map, right, left, cost);
            }
        
            return map;
        };
        
        var tableToString = (table) => {
            return Object.keys(table)
            .map(vertex => {
                var { vertex: from, cost } = table[vertex];
                return `${vertex}: ${cost} via ${from}`;
            })
            .join('\n');
        };
        
        var tracePath = (table, start, end) => {
            var path = [];
            var next = end;
            while (true) {
            path.unshift(next);
            if (next === start) { break; }
            next = table[next].vertex;
            }
        
            return path;
        };
        
        var run = (graph, start, end) => {
            var map = graphToMap(graph);
        
            // console.log(map);
            var visited = [];
            var frontier = [start];
            var table = { [start]: { vertex: start, cost: 0 } };
        
            var vertex;
            while (vertex = frontier.shift()) {
            // Explore unvisited neighbors
            var neighbors = map[vertex]
                .filter(n => !visited.includes(n.vertex));
        
            // Add neighbors to the frontier
            frontier.push(...neighbors.map(n => n.vertex));
        
            var costToVertex = table[vertex].cost;
        
            for (let { vertex: to, cost } of neighbors) {
                var currCostToNeighbor = table[to] && table[to].cost;
                var newCostToNeighbor = costToVertex + cost;
                if (currCostToNeighbor == undefined ||
                    newCostToNeighbor < currCostToNeighbor) {
                // Update the table
                table[to] = { vertex, cost: newCostToNeighbor };
                }
            }
        
            visited.push(vertex);
            }
        
            // console.log(table);
        
            console.log('Here you go:');
            console.log(tableToString(table));
        
            var path1 = tracePath(table, start, end);
            
            for(var i=0; i<path1.length; i++){
                switch(path1[i]){
                    case 'A': path1[i] = 'KUL'; break;
                    case 'B': path1[i] = 'ICN'; break;
                    case 'C': path1[i] = 'ITM'; break;
                    case 'D': path1[i] = 'MEL'; break;
                    case 'E': path1[i] = 'SVO'; break;
                    case 'F': path1[i] = 'PEK'; break;
                    case 'G': path1[i] = 'CGK'; break;
                    case 'H': path1[i] = 'SIN'; break;
                    case 'I': path1[i] = 'JFK'; break;
                    case 'J': path1[i] = 'MAN'; break;
                    case 'K': path1[i] = 'MAD'; break;
                }
            };
            if (path1.length > 0) {
                document.getElementById("result").innerHTML = path1.join('->');
            }
            
        };
        run(graph, "<?php echo $from ?>", "<?php echo $to ?>");
      </script>
    </div>
  </body>
</html>