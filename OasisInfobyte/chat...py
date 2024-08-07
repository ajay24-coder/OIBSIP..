import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 12345))

print("Connected to server. Start chatting!")

while True:
    # Send message to server
    message = input("Client: ")
    client_socket.send(message.encode())

    # Receive message from server
    message = client_socket.recv(1024).decode()
    print(f"Server: {message}")

# Close socket
client_socket.close()