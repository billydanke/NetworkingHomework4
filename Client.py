import socket

client_name = "Aaron's Client"

# Prompt for a number 1 to 100
client_number = int(input("Enter an integer between 1 and 100: "))

# make sure the number is in range
assert 1 <= client_number <= 100, "Number must be between 1 and 100."

# Create a socket and connect to server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 42069))
    
    # Send the client name and number to the server
    message = f"{client_name},{client_number}"
    s.sendall(message.encode('utf-8'))
    print("Message sent.")
    
    # Display the server response
    data = s.recv(1024).decode('utf-8')
    print("Recieved response from server.")
    server_name, server_number = data.split(',')
    server_number = int(server_number)
    
    print(f"Client's Name: {client_name}")
    print(f"Server's Name: {server_name}")
    print(f"Client's Number: {client_number}, Server's Number: {server_number}, Sum: {client_number + server_number}")