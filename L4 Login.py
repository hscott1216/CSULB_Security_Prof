"""
Lab Task
Create a login interface using sockets.

1. Create basic server and client sockets.
2. Add a welcome message and ask for a user name upon connection.
3. Ask for a password from the client after entering the user name.
4. Create a step that checks if the correct user name and password were entered.
"""

import socket

s = socket.socket()
s.connect(("127.0.0.1", 1337))
welcome_message = s.recv(2048).decode()
print(welcome_message)
username = input("")
s.send(username.encode())
ans = s.recv(1024).decode()
print(ans)
password = input("")
s.send(password.encode())
ans = s.recv(2048).decode()
print(ans)
s.close()
