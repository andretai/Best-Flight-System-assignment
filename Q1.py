import gmplot

#Kuala Lumpur, Incheon, Osaka, Melbourne, Moscow, Beijing, Jakarta, Singapore, New York, Manchester, Madrid
latitude_list = [2.745537, 37.460353, 34.789594, -37.665357, 55.410343, 40.085148, -6.127211, 1.364860, 40.760284, 53.358796, 40.498275]
longitude_list = [101.707316, 126.440674, 135.438084, 144.840642, 37.902312, 116.552407, 106.653684, 103.991594, -73.772304, -2.272773, -3.567727]

gmap3 = gmplot.GoogleMapPlotter(2.745537, 101.707316, 13)

#Adding Google Maps API key
gmap3.apikey = "AIzaSyAGADiifvUELmMdOfy-UKlHPxNI6rrJUFE"

#Plotting using HeatMap
gmap3.heatmap( latitude_list, longitude_list )
gmap3.draw("mymap.html")


"""
Methods of plotting a marker in a base map:
gmap3.scatter  //drawing a point
gmap3.plot  //drawing a line
gmap3.heatmap  //drawing heatmap
gmap3.draw("mymap.html")  //drawing markers into a base map
"""
