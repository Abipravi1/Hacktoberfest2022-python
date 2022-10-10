import socket
import time

host = "0.0.0.0"
port = 5555
# socket will work on UDP protocol
# initializing the socket
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind the host and the port to communicate
soc.bind((host, port))
# the file where the gps data will go
filestr = open('gps_data.txt', 'w')

try:
    # loop which will continuously get the gps data
    while True:
        print("waiting...")
        # this is used to receive the message UDP protocol
        message, address = soc.recvfrom(4200)  # number of bytes needed to read = 4200
        # writing the gps coordinates in this file
        filestr.write(str(message) + "\n")
        time.sleep(1)
        print("received message: ", str(message))

finally:
    filestr.close()
