import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")

latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation_data = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000<=elevation<3000:
        return "orange"
    else:
        return "red" 
    
map = folium.Map(location=[51.16,71.47],zoom_start=6) # creates a map object with coordinates of latitude and longitude, and zooms to this location (Nur-Sultan, Kazakhstan)

fgv = folium.FeatureGroup(name="Volcanoes in USA")

for lat,lon,el in zip(latitude,longitude,elevation_data):
    #popup = folium.Popup(str(el), parse_html=True)
    fgv.add_child(folium.CircleMarker(location=[lat,lon], radius = 6, popup=str(el)+" m",
                                    fill_color=color_producer(el), color="grey",fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read()),
             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 
                                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
                                            else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html") # saves that object into html file


