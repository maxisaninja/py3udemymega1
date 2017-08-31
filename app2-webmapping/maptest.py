import folium
import pandas

def ele_to_color(el):
    if el < 1500:
        return "green"
    elif el < 3000:
        return "orange"
    elif el < 5000:
        return "red"
    else:
        return "purple"
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
ele = list(data["ELEV"])
map = folium.Map(location=[43.056649, -73.389955], zoom_start=5,
    tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, ele):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=5,
    popup=str(el)+"m", color=ele_to_color(el)))
foog = folium.FeatureGroup(name="Country populations")
foog.add_child(folium.GeoJson(data=open("world.json", 'r',encoding="utf-8-sig"),
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fg)
map.add_child(foog)
map.add_child(folium.LayerControl())

map.save("Map1.html")
