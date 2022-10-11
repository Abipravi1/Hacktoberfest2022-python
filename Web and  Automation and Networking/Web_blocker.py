# Script for blocking certain websites. U can put ur list website 

import time
from datetime import datetime as dt

hosts_path = r"/etc/hosts" # r is for raw string
hosts_temp = "hosts"

#Locahost's IP
redirect = "127.0.0.1"

# Put ur desired website to block it
web_list = ["www.facebook.com", "facebook.com"]

while True:
    # Time of the users work
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 22):
        print("Working hours")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in web_list:
                if website in content:
                    pass
                else:
                    file.writable(redirect+" "+website+"\n")

    else:
        print("No ad, no pain")
