#Comparing distance between All the cities
from geopy.distance import great_circle #Lib to get dist between two points
from geopy.geocoders import Nominatim #Lib to geolocate an address
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut

geolocator = Nominatim(user_agent="app")
origin_list = ["Kuala Lumpur International Airport", "Incheon International Airport", "Osaka International Airport", "Melbourne Airport", "Shanghai Pudong International Airport", "Soekarno-Hatta International Airport", "Changi Airport Singapore", "John F. Kennedy International Airport", "Manchester Airport", "Madrid Barajas Airport"]
dest_list = ["Kuala Lumpur International Airport", "Incheon International Airport", "Osaka International Airport", "Melbourne Airport", "Shanghai Pudong International Airport", "Soekarno-Hatta International Airport", "Changi Airport Singapore", "John F. Kennedy International Airport", "Manchester Airport", "Madrid Barajas Airport"]

for originInput in origin_list:
    for destInput in dest_list:
        originGeolocate = geolocator.geocode(str(originInput))

        newOrigin = (originGeolocate.latitude, originGeolocate.longitude)

        destGeolocate = geolocator.geocode(str(destInput))

        newDest = (destGeolocate.latitude, destGeolocate.longitude)
        print("Origin: " + str(originInput) + str(newOrigin) + "Dest: " + str(destInput) + str(newDest))
        print("Distance between " + str(originInput) + " and " + str(destInput) + ": " + str(geodesic(newOrigin, newDest).kilometers) + " KM")
