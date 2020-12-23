"""
Lab Task
Create a basic server socket and test connectivity using Netcat.

1. Open a new project in PyCharm and create a listening server for the socket
library to be imported. The server will listen to all addresses on port 4444 and
allow only one connection.

2. After it is created, the socket will be closed.

3. Run nc 127.0.0.1 4444 via the CMD or terminal.


"""


import socket # import the Socket module 

serverSocket = socket.socket() # initiate a socket for the server  called serverSocket 
serverSocket.bind(("0.0.0.0",4444)) # set it to accept a session from any IP to port 4444
serverSocket.listen(4) # on allow 1 connection, after the first close off the port.

conn, addr = serverSocket.accept() # capture new socket object and the address bound 
                                   # to the socket object. 
print(conn,addr)

"""
I have not been able to get a connection on any port 
"""