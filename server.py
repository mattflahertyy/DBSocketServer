import socket

"""
**********   PYTHON DATABASE SOCKET (SERVER)   **********

This program creates a socket server and stores customer data from a text file into memory. Once a client
connects to the socket, a menu is provided allowing them to find, add and delete customers. They can also
update the age, phone number, home address, and display a list of the customers sorted by their name.
Once the client disconnects, the server remains running, waiting for a new client to connect to the socket.

Programmed by Matthew Flaherty
LinkedIn: www.linkedin.com/in/matthewflaherty9
"""

# function for finding customer
def findCust():
    # asking client to enter a name
    clientConnected.send("Customer Name: ".encode())
    # receiving menu selection
    name = clientConnected.recv(1024)
    name = name.decode('utf-8')


    # search for the customer in the database
    count = 0
    found = False
    for i in dataBase:
        if dataBase[count][0] == name:
            found = True
            break
        count += 1

    # if customer is found, send the customer info to client, if not found display not found message
    if found:
        customer_data = ""
        for item in dataBase[count]:
            customer_data += item
            customer_data += "|"
        customer_data += "\n\n"
        clientConnected.send(customer_data.encode())
    else:
        name += " not found in database\n"
        clientConnected.send(name.encode())

# function for adding customer
def addCust():
    # displaying adding customer message to client and asks to input name
    clientConnected.send("*****Adding Customer*****\nEnter Customer Name: ".encode())
    # checking if name exists, loops and asks to re-enter if name is invalid
    nameExists = None
    name = ""
    # loop until name has been found
    while not (nameExists == False):
        # receiving name from client
        name = clientConnected.recv(1024)
        name = name.decode('utf-8')

        # check if name exists in memory
        count = 0
        for i in dataBase:
            if dataBase[count][0] == name:
                nameExists = True
                clientConnected.send("Error! Name already exists, please enter a different name:".encode())
                break
            count += 1
        if count == len(dataBase):
            nameExists = False

    # asking client to enter an age
    clientConnected.send("Enter Customer Age: ".encode())
    age = clientConnected.recv(1024)
    age = age.decode('utf-8')

    # loops and asks to re-enter if age is invalid
    while (not int(age.isdigit())) or not (0 < int(age) <= 101):
        clientConnected.send("Error! Please enter a valid age between 1 and 100:".encode())
        age = clientConnected.recv(1024)
        age = age.decode('utf-8')

    # asking client to enter an address
    clientConnected.send("Enter Customer Address: ".encode())
    address = clientConnected.recv(1024)
    address = address.decode('utf-8')

    # asking client to enter a phone number
    clientConnected.send("Enter Customer Phone Number: ".encode())
    phone = clientConnected.recv(1024)
    phone = phone.decode('utf-8')

    # store new data in a list
    newCustomer = [name, age, address, phone]

    # add new list to the end of data list
    dataBase.append(newCustomer)

    # display success message
    clientConnected.send("Customer added successfully\n".encode())

# function for deleting customer
def delCust():
    # displaying deleting customer message to client and asks to input name
    clientConnected.send("*****Deleting Customer*****\nEnter Customer Name: ".encode())

    # receiving data from client
    name = clientConnected.recv(1024)
    name = name.decode('utf-8')

    nameExists = None
    count = 0
    # check if name is in database
    for i in dataBase:
        if dataBase[count][0] == name:
            nameExists = True
            break
        count += 1

    # if name exists remove the customer from database and display removed message to client
    if nameExists:
        dataBase.remove(dataBase[count])
        clientConnected.send("Customer successfully removed.\n".encode())
    else:
        clientConnected.send("Customer doesnt exist.\n".encode())

# function for updating age
def updateAge():
    # displaying adding customer message to client and asks to input name
    clientConnected.send("*****Updating Customer Age*****\nEnter Customer Name: ".encode())

    name = clientConnected.recv(1024)
    name = name.decode('utf-8')

    nameExists = None
    count = 0
    # check if name is in database
    for i in dataBase:
        if dataBase[count][0] == name:
            nameExists = True
            break
        count += 1

    # if name is valid, asks to enter new age and checks if valid integer and between 1 and 100
    if nameExists:
        clientConnected.send("Please enter the new age:".encode())
        age = clientConnected.recv(1024)
        age = age.decode('utf-8')
        while (not int(age.isdigit())) or not (0 < int(age) <= 101):
            clientConnected.send("Error! Please enter a valid age between 1 and 100:".encode())
            age = clientConnected.recv(1024)
            age = age.decode('utf-8')

        # update age in database
        dataBase[count][1] = age

        # display success message to client
        clientConnected.send("Age updated successfully.\n".encode())
    else:
        # display fail message to client
        clientConnected.send("Customer not found.\n".encode())

# function for updating address
def updateAddress():
    # displaying adding customer message to client and asks to input name
    clientConnected.send("*****Updating Customer Home Address*****\nEnter Customer Name: ".encode())

    # receiving data from client and converting to utf8
    name = clientConnected.recv(1024)
    name = name.decode('utf-8')

    nameExists = None
    count = 0
    # check if name exists
    for i in dataBase:
        if dataBase[count][0] == name:
            nameExists = True
            break
        count += 1

    # asks for address and sends to client
    if nameExists:
        clientConnected.send("Please enter the new home address:".encode())
        address = clientConnected.recv(1024)
        address = address.decode('utf-8')

        # updating address in database
        dataBase[count][2] = address

        # display success message to client
        clientConnected.send("Home address updated successfully\n".encode())
    else:
        clientConnected.send("Customer not found.\n".encode())

# function for updating phone number
def updatePhone():
    # displaying adding customer message to client and asks to input name
    clientConnected.send("*****Updating Customer Phone Number*****\nEnter Customer Name: ".encode())

    # receiving data from client and converting to utf8
    name = clientConnected.recv(1024)
    name = name.decode('utf-8')

    # check if name exists in database
    nameExists = None
    count = 0
    for i in dataBase:
        if dataBase[count][0] == name:
            nameExists = True
            break
        count += 1

    # asks client to enter phone number and receives number
    if nameExists:
        clientConnected.send("Please enter the new phone number:".encode())
        phone = clientConnected.recv(1024)
        phone = phone.decode('utf-8')

        # updates number in database
        dataBase[count][3] = phone

        # display success message to client
        clientConnected.send("Phone number updated successfully\n".encode())
    else:
        clientConnected.send("Customer not found.\n".encode())

# function for printing the report
def printReport():
    # sorting the database by name
    sortedDataBase = sorted(dataBase, key=lambda l: l[0], reverse=False)

    # store all sorted customer data to a string
    reportText = "** Python DB contents **\n"
    for row in sortedDataBase:
        count = 0
        for item in row:
            reportText += item
            if not count == 3:
                reportText += "|"
            count += 1

        reportText += "\n"

    # send sorted data to client
    clientConnected.send(reportText.encode())

def exitCode():
    # display goodbye message to client
    clientConnected.send("Closing connection with server... Goodbye!".encode())

# this menu displays the database menu
def callMenu():
    menu_selection = 0
    # loop until client selects to exit (8)
    while not (menu_selection == 8):

        menu = "Python DB Menu\n1. Find Customer\n2. Add customer\n3. Delete Customer\n4. Update customer age\n5. " \
               "Update customer address\n6. Update customer phone\n7. Print report\n8. Exit\n\nSelect: "

        # sending menu message to client
        clientConnected.send(menu.encode())

        # receiving menu selection
        menu_selection = clientConnected.recv(1024)
        menu_selection = menu_selection.decode('utf-8')

        # loop if menu selection isn't a digit or valid choice, ask client to input again
        while (not int(menu_selection.isdigit())) or not (1 <= int(menu_selection) <= 8):
            digit_error = "Error! Please enter a valid age between 1 and 8:"
            clientConnected.send(digit_error.encode())
            menu_selection = clientConnected.recv(1024)
            menu_selection = menu_selection.decode('utf-8')

        menu_selection = int(menu_selection)

        # decide which function to choose based on client menu input
        if menu_selection == 1:
            findCust()
        elif menu_selection == 2:
            addCust()
        elif menu_selection == 3:
            delCust()
        elif menu_selection == 4:
            updateAge()
        elif menu_selection == 5:
            updateAddress()
        elif menu_selection == 6:
            updatePhone()
        elif menu_selection == 7:
            printReport()
        elif menu_selection == 8:
            exitCode()

# --------------------------------     Storing data in text file in a list     --------------------------------
file = open('data.txt', 'r')

# store all lines in text file to list
Lines = file.readlines()
dataBase = []

# loop through each line in list, splitting the |, creating a list of lists
numOfDataSet = 0
for line in Lines:
    line = line.rstrip('\n')
    dataBase.append(line.split('|'))

    # remove left/right white line characters
    count2 = 0
    for entry in dataBase[numOfDataSet]:
        entry = dataBase[numOfDataSet][count2]
        dataBase[numOfDataSet][count2] = entry.strip()
        count2 += 1

    # removes from list if name does not contain letters
    if not dataBase[numOfDataSet][0].isalpha():
        dataBase.pop()
    else:
        numOfDataSet += 1

# check to see if name already exists, remove duplicates
currentIdx = 0
for customer in dataBase:
    checkingIdx = 0
    while checkingIdx < len(dataBase):
        if customer[0] == dataBase[checkingIdx][0] and currentIdx != checkingIdx:
            dataBase.remove(dataBase[checkingIdx])
        else:
            checkingIdx += 1
    currentIdx += 1

# --------------------------------     SOCKET     --------------------------------
while True:
    # create the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind and listen
    server.bind(("localhost", 9999))
    server.listen()

    # Accept connections
    while True:
        (clientConnected, clientAddress) = server.accept()

        # print message displaying client connection address
        print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]))

        # begin by calling method to display DB menu
        callMenu()
