import folium
print(dir(folium))

map= folium.Map(location=[44.983410,-85.773460], zoom_start= 7)

print(map)

print(dir(folium.Map))
print(map.save('test.html'))

map2 = folium.Map(location=[44.983410,-85.773460], zoom_start=15, tiles= "Stamen Terrain")
print(map2)
print(map2.save("test2.html"))

