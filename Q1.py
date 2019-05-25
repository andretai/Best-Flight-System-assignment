# import gmplot
# gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)
# #Adding Google Maps API key
# gmap.apikey = "AIzaSyAGADiifvUELmMdOfy-UKlHPxNI6rrJUFE"
#
# gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
# gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
# gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
# gmap.heatmap(heat_lats, heat_lngs)
#
# gmap.draw("mymap.html")

#Test2
# import gmplot package
import gmplot

#Kuala Lumpur, South Korea, Osaka, Melbourne, ShangHai,  Jakarta, Singapore, New York, Manchester, Madrid
latitude_list=[2.745537,37.460353,34.789594,-37.665357,31.144990,-6.127211,1.364860,40.760284,53.358796,40.498275]
longitude_list=[101.707316,126.440674,135.438084,144.840642,121.808304,106.653684,103.991594,-73.772304,-2.272773,-3.567727]

gmap3 = gmplot.GoogleMapPlotter(2.745537, 101.707316, 13)

#Adding Google Maps API key
gmap3.apikey = "AIzaSyAGADiifvUELmMdOfy-UKlHPxNI6rrJUFE"

# # scatter method of map object
# # scatter points on the google map
# gmap3.scatter(latitude_list, longitude_list, '# FF0000',size=40, marker=False)

# # Plot method Draw a line in
# # between given coordinates
# gmap3.plot(latitude_list, longitude_list,'worldAirport', edge_width=2.5)

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