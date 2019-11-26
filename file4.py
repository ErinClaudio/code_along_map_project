import folium
import pandas as pd

map4 = folium.Map(location=[44.983410, -85.773460], zoom_start=7, tiles='Stamen Terrain')

df = pd.read_csv('Volcano.txt')

for lat,lan,name in zip(df['LAT'], df['LON'], df['NAME']):
    folium.Marker(location=[lat,lan],popup=name, icon=folium.Icon(icon='cloud')).add_to(map4)

print(map4.save('test4.html'))

map5 = folium.Map(location=[44.983410, -85.773460], zoom_start=7, tiles='Stamen Terrain')
df = pd.read_csv('Volcano.txt')

for lat,lan,name,elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(location=[lat,lan],popup=name, icon=folium.Icon(color ='green' if elev in range (0,1000) else "orange" if elev in range (1001,1999) else 'blue' if elev in range(2000,2999)else 'red',icon = 'cloud')).add_to(map5)

print(map5.save('test5.html'))
