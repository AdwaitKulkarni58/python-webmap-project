import folium
import pandas

file_name = pandas.read_csv("volcanoes.txt")
latitude_list = list(file_name["LAT"])
longitude_list = list(file_name["LON"])

map = folium.Map(location=[49.282, -123.120], tiles="Stamen Terrain")
feature_group = folium.FeatureGroup(name="Map")
for lat, lon in zip(latitude_list, longitude_list):
    feature_group.add_child(folium.Marker(location=[lat, lon], popup="Marker", icon=folium.Icon(color="green")))
    map.add_child(feature_group)
map.save("Map.html")