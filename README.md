# DBSocketServer
Overview:
This Python project is a client/server database program. The server manages a customer database from a text file. Clients interact through a menu, performing operations like finding, adding, updating, and deleting records. Server loads data, performs error checks, ensuring a seamless user experience.


Client/Server Architecture:
- Utilizes Python's SocketServer class for easy implementation.
- Single-client interaction to simplify concerns about concurrency and thread control.


Database Loading:
- The server loads customer records from a plain text file named data.txt.
- Each customer record is a tuple containing name, age, address, and phone number.
- Data file is formatted with one record per line, fields separated by '|'.
- Basic error checking ensures data integrity during loading.


Client Menu Interface:
- The client application presents a menu for the user to choose from various database operations.
- Options include finding, adding, updating, deleting, and printing customer records, as well as exiting the application.


Database Operations:
- Find Customer: 
    Retrieves and displays customer information based on user-provided name. Provides appropriate feedback if the customer is not found.
- Add Customer:
    Allows the user to input new customer details, with server confirmation or a message indicating if the customer already exists.
- Delete Customer:
    Removes a specified customer and provides feedback on success or failure.
- Update Customer:
    Supports updating customer age, address, and phone number. Validates the provided name and displays appropriate messages.
- Print Report:
    Displays the contents of the database sorted by customer name, ensuring the integrity of the server's functionality.

Termination:
- The client application terminates , displaying a goodbye message upon choosing the exit option.
- The server process continues running in an infinite loop, allowing the client to reconnect if restarted.
