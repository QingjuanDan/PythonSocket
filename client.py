import socket

def start_client():
    client_number = int(input("Enter an integer between 1 and 100: "))
    if client_number < 1 or client_number > 100:
        print("Invalid number. Exiting.")
        return

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('10.245.194.202', 5050))  # Connect to the server on localhost port 5050
    client_name = "Client of John Q. Smith"
    client_message = f"{client_name};{client_number}"
    client.send(client_message.encode())

    server_response = client.recv(1024).decode()
    server_name, server_number_str = server_response.split(';')
    server_number = int(server_number_str)
    sum_numbers = client_number + server_number
    print(f"Client: {client_name}, Server: {server_name}")
    print(f"Client's number: {client_number}, Server's number: {server_number}, Sum: {sum_numbers}")

    client.close()

if __name__ == "__main__":
    start_client()
