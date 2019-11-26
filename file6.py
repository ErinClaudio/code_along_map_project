import folium
import pandas as pd


df = pd.read_csv('Volcano.txt')

latemean = df['LAT'].mean()
lonmean = df['LON'].mean()

map6 = folium.Map(location=[latemean, lonmean], zoom_start=5, tiles='Stamen Terrain')


def color(elev):
    if elev in range(0, 1000):
        col = 'pink'
    elif elev in range(1001, 1999):
        col = 'darkpurple'
    elif elev in range(2000, 2999):
        col = 'darkred'
    else:
        col = 'beige'
    return col


for lat, lan, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(location=[lat, lan], popup=name, icon=folium.Icon(color = color(elev), icon='cloud')).add_to(map6)

print(map6.save("test7.html"))
