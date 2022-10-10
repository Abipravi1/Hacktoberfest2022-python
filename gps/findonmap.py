import folium

map = folium.Map(location=[28.18, 77.00])
folium.Marker(location=[28.18, 77.00]).add_to(map)

map.save('display.html')

