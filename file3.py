import folium

map3 = folium.Map(location=[44.983410, -85.773460], zoom_start = 15, tiles='Stamen Terrain')

folium.Marker(location=[44.983410, -85.773460], popup='I am so lost', icon=folium.Icon(icon="cloud")).add_to(map3)

folium.Marker(location=[44.983410, -85.773460], popup='But I can see you', icon=folium.Icon(color='green')).add_to(map3)

print (map3)
print(map3.save('test3.html'))



