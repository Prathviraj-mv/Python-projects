import folium
import requests
from geopy.distance import geodesic

# iss position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
lat = float(data["iss_position"]["latitude"])
long = float(data['iss_position']['longitude'])
cord1 = (lat, long)
# my position
my_lat = float(12.29581)
my_long = float(76.639381)
cord2 = (my_lat, my_long)

# map
m = folium.Map(location=[lat, long], zoom_start=3)
folium.Marker([lat, long], popup="ISS", icon=folium.features.CustomIcon("iss.png")).add_to(m)
folium.Marker([my_lat, my_long], popup="MY_location", icon=folium.Icon(icon="home", color="red")).add_to(m)

# distance
line = folium.PolyLine(locations=[[my_lat, my_long], [lat, long]], color='blue').add_to(m)
distance_btw = geodesic(cord1, cord2).kilometers

distance_text = f"distance ={distance_btw:.2f}km"
folium.Marker([lat - 10, long - 20], popup=distance_text, icon=folium.Icon(icon="cloud", color="blue")).add_to(m)

m.save("map.html")
