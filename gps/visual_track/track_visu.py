import folium

gps_list = []
vib_red_list = []
i = 0
with open("track1.txt" ,"r" )as file:
    for elem in file:

        #print(elem)
        raw_str = elem.strip()
        raw_list = list(raw_str.split(","))
        time_data = (raw_list[0:4])
        lat = raw_list[4].replace("Latitude: ","").strip()
        lon = raw_list[5].replace("Longitude: ","").strip()
        alt = raw_list[6].replace("Altitude: ","").strip()
        vib = raw_list[14].strip()
        #gps_data = time_data, lat,lon,alt,vib
        gps_data = (float(lat), float(lon))#,float(vib))
        gps_list.append(gps_data)
        if float(vib) > 1.3:
            data = (float(lat), float(lon),str("red"),vib)
            vib_red_list.append(data)


        i +=1


#print(gps_list)

m = folium.Map(location=gps_list[0],
              zoom_start=15)
#make route
loc = gps_list
folium.PolyLine(loc,
                color= 'blue',
                weight=10,
                opacity=0.8).add_to(m)
m

for elem in vib_red_list:  #add circle to bad points
    print(elem)
    marker = folium.CircleMarker(elem[:2],radius= 4,color=elem[2], popup="Attention" )
    marker.add_to(m)


m.save('route.html')