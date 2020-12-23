"""
this is the server side of lab 3 

"""


import socket # import the Socket module

serverSocket = socket.socket() # initiate a socket for the server  called serverSocket
serverSocket.bind(("0.0.0.0",4444)) # set it to accept a session from any IP to port 4444
serverSocket.listen(4) # on allow 4 connection, after the first close off the port.
conn, addr = serverSocket.accept() # capture new socket object and the address bound
                                   # to the socket object.
#serverSocket.send("Hello, I'm the server".encode())
serverSocket.send("Exit".encode())



mysocket.close()  # close the connection
