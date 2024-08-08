import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a address and port
server_socket.bind(('localhost', 12345))

# Listen for incoming connections
server_socket.listen(1)

print("Server started. Waiting for incoming connection...")

# Accept incoming connection
client_socket, address = server_socket.accept()

print(f"Connected to {address}")

while True:
    # Receive message from client
    message = client_socket.recv(1024).decode()
    print(f"Client: {message}")

    # Send message back to client
    message = input("Server: ")
    client_socket.send(message.encode())

# Close sockets
client_socket.close()
server_socket.close()