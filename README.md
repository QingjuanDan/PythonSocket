# Python Socket Programming Project

This project consists of a simple client-server application using Python's socket programming capabilities. The server listens for connections from clients, receives an integer and a name string from each client, performs a calculation, and sends a response back. This README outlines how to set up and run the server and client scripts.

## Project Structure

- `server.py`: The server script that listens for incoming connections and handles client requests.
- `client.py`: The client script that connects to the server, sends data, and receives a response.

## Requirements

- Python 2.7 or Python 3.x (The instructions below assume Python 3.x. Adjust commands for Python 2.7 where necessary.)
- Network access if running client and server on different machines (adjust firewall settings accordingly)

## Setup Instructions

1. **Ensure Python is Installed**: Check your Python version by running `python --version` or `python3 --version` in your terminal. This project requires Python 2.7 or later.

2. **Download Project Files**: Clone or download the project files to your local machine.

3. **Navigate to Project Directory**: Use the terminal to navigate to the directory containing `server.py` and `client.py`.

## Running the Server

1. Open a terminal window.
2. Navigate to the project directory.
3. Run the server script:
   ```bash
   python3 server.py
he server will start and listen for incoming connections. Keep this terminal open.

Running the Client

1.Open a new terminal window (leave the server running).
2.Navigate to the project directory.
3.Run the client script:
```
python3 client.py
```
4.Follow any on-screen prompts in the client script (e.g., entering an integer between 1 and 100).

Customizing the Scripts

To change the port the server listens on, edit server.py and modify the server.bind(('0.0.0.0', 5050)) line with your desired port.
To connect the client to a different server or port, edit client.py and modify the client.connect(('localhost', 5050)) line accordingly.

Troubleshooting

Connection Refused: Ensure the server is running before starting the client. Check that firewalls are not blocking the connection.
Invalid Input: The client script requires an integer input within a specified range. Ensure your input matches these criteria.
Contributing

Feel free to fork this project, make improvements, and submit pull requests. We appreciate your contributions to enhancing this learning tool.

License

This project is open-source and available under the MIT License.
