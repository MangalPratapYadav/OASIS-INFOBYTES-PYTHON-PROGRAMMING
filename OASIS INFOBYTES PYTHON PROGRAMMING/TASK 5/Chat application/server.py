import socket
from threading import Thread

def handle_client(client_socket, client_address, client_name):
    print(f"{client_name} ({client_address[0]}:{client_address[1]}) joined the chat.")
    broadcast(f"{client_name} has joined the chat!", None)

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            if message.strip() == "/exit":
                broadcast(f"{client_name} has left the chat!", None)
                print(f"{client_name} has left the chat.")
                break
            print(f"{client_name}: {message}")
            broadcast(f"{client_name}: {message}", client_socket)
        except (ConnectionResetError, ConnectionAbortedError):
            break

    clients.remove((client_socket, client_name))
    client_socket.close()
    broadcast(f"{client_name} has left the chat!", None)
    print(f"{client_name} has left the chat.")

def broadcast(message, sender_socket):
    for client_socket, _ in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode("utf-8"))
            except:
                client_socket.close()
                clients.remove((client_socket, _))

def server_chat():
    while True:
        message = input()
        if message.strip() == "/exit":
            print("Server shutting down...")
            for client_socket, _ in clients:
                client_socket.close()
            host_socket.close()
            break
        broadcast(f"{server_name}: {message}", None)
        print(f"{server_name}: {message}")

host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host_ip = "127.0.0.1"
port_number = 7500
host_socket.bind((host_ip, port_number))
host_socket.listen()

server_name = input("Enter your name (server admin): ")
print(f"{server_name}'s server is running and waiting for connections...")

clients = []

Thread(target=server_chat, daemon=True).start()

while True:
    try:
        client_socket, client_address = host_socket.accept()
        client_socket.send("Enter your name: ".encode("utf-8"))
        client_name = client_socket.recv(1024).decode("utf-8")
        clients.append((client_socket, client_name))

        broadcast(f"{client_name} has joined the chat!", None)

        Thread(target=handle_client, args=(client_socket, client_address, client_name), daemon=True).start()
    except:
        break
