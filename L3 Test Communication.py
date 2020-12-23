"""
Lab Task
Create basic connectivity between the client and server sockets.

1. Run both previously created scripts (Client socket and Server socket) and set the
parameters to establish basic communication between the two, using the recv()
function on the client side.

2. Set the send() function on the server side to establish communication with the
client that will receive messages from the server.

"""

import time # this module allows for the mangement of time
import socket # socketes allow for the creation of network pipes

mysocket = socket.socket() # My socket var
mysocket.connect(("127.0.0.1", 4444)) # Client will attempt to create connection

Data = mysocket.recv(2048).decode # recive data from the server.
print(Data)
if Data == "exit":
    print("closing Conection ")
    time.sleep(15) #delay 15 seconds
    mysocket.close() #close the connection


