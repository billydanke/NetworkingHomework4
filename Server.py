import socket

server_name = "Aaron's Server"
server_number = 42  # This is the server's magic number

# Make the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 42069))
    s.listen()

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connection from {addr}")

            # Receive data from the client
            data = conn.recv(1024).decode('utf-8')
            print("Received data from client")
            client_name, client_number = data.split(',')
            client_number = int(client_number)

            if 1 <= client_number <= 100:
                # Display client and server names, and numbers
                print(f"Client's Name: {client_name}")
                print(f"Server's Name: {server_name}")
                print(f"Client's Number: {client_number}, Server's Number: {server_number}, Sum: {client_number + server_number}")

                # Send server's name and number back to the client
                response = f"{server_name},{server_number}"
                conn.sendall(response.encode('utf-8'))
                print("Sent response.")
            else:
                print("Received bad integer. Shutting down.")
                break