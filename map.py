import folium
import pandas

file_name = pandas.read_csv("volcanoes.txt")
latitude_list = list(file_name["LAT"])
longitude_list = list(file_name["LON"])
elevation_list = list(file_name["ELEV"])

def decideColor(elevation):
    if (elevation < 1000):
        return 'green'
    elif (1000 <= elevation <= 3000):
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[49.282, -123.120], tiles="Stamen Terrain")
feature_group = folium.FeatureGroup(name="Map")
for lat, lon, el in zip(latitude_list, longitude_list, elevation_list):
    feature_group.add_child(folium.Marker(location=[lat, lon], popup=str(el) + " m", icon=folium.Icon(color=decideColor(el))))
    map.add_child(feature_group)
map.save("Map.html")