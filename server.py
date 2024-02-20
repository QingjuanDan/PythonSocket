import socket
import threading

def handle_client_connection(client_socket):
    try:
        client_message = client_socket.recv(1024).decode()
        client_name, client_number_str = client_message.split(';')
        client_number = int(client_number_str)
        if client_number < 1 or client_number > 100:
            print("Received out-of-range integer. Shutting down.")
            return
        server_number = 42  # Example server number, can be randomized
        sum_numbers = client_number + server_number
        print(f"Client: {client_name}, Server: Server of John Q. Smith")
        print(f"Client's number: {client_number}, Server's number: {server_number}, Sum: {sum_numbers}")
        server_response = f"Server of John Q. Smith;{server_number}"
        client_socket.send(server_response.encode())
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5050))  # Bind to port 5050 on all available interfaces
    server.listen(5)
    print("Server listening on port 5050...")
    try:
        while True:
            client_sock, address = server.accept()
            print(f"Accepted connection from {address}")
            client_handler = threading.Thread(
                target=handle_client_connection,
                args=(client_sock,)
            )
            client_handler.start()
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
