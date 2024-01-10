import socket

"""
**********   PYTHON DATABASE SOCKET (CLIENT)   **********

This program creates a socket server and stores customer data from a text file into memory. Once a client
connects to the socket, a menu is provided allowing them to find, add and delete customers. They can also
update the age, phone number, home address, and display a list of the customers sorted by their name.
Once the client disconnects, the server remains running, waiting for a new client to connect to the socket.

Programmed by Matthew Flaherty
LinkedIn: www.linkedin.com/in/matthewflaherty9
"""

# Create a client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(("localhost", 9999))

while True:
    # Receive data from server
    dataFromServer = client.recv(1024)

    # Decode received data into UTF-8
    dataFromServer = dataFromServer.decode('utf-8')

    # print message from server
    print(dataFromServer)

    # if the message contains goodbye, close the clients connection
    if "Goodbye" in dataFromServer:
        break

    # if the message contains a colon symbol, this indicates the client needs to input and send back to the server
    if ":" in dataFromServer:
        # print("true")
        client_input = input()
        client.send(client_input.encode())
