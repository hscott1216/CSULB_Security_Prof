"""
Lab Task: Client Socket 
Create a basic client socket, test connectivity using Netcat, and wait 30 seconds. 
1 Import both the socket and time libraries. 
2 Run nc -Ivp 1424 via the CMD or terminal to start a listening server. 
3 Connect to the listener using a socket.socket() object. 
Create a 30-second delay before the socket closes. 
4 Verify that the connection was established. 


nc -lvp 192.168.86.45 1424
"""

import time # this module allows for the mangement of time
import socket # socketes allow for the creation of network pipes

mysocket = socket.socket() # My socket var
#mysocket.connect(('192.168.86.90', 1424)) # Client will attempt to create connection
mysocket.connect(('192.168.86.90', 1424))
time.sleep(30) #delay 30 seconds
print("closing Conection ")

mysocket.close() #close the connection

