import socket
from threading import Thread

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(message)
        except ConnectionResetError:
            print("Connection lost!")
            break
    client_socket.close()

def send_messages():
    while True:
        message = input()
        if message.strip() == "/exit":
            client_socket.send(message.encode("utf-8"))
            print("You have left the chat.")
            break
        else:
            try:
                client_socket.send(message.encode("utf-8"))
            except:
                print("Unable to send message!")
                break
    client_socket.close()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = "127.0.0.1"
port_number = 7500

try:
    client_socket.connect((host_ip, port_number))
except ConnectionRefusedError:
    print("Unable to connect to the server. Ensure the server is running.")
    exit()

print(client_socket.recv(1024).decode("utf-8"))
client_name = input("Your name: ")
client_socket.send(client_name.encode("utf-8"))

print("Connected to the chat server!")

Thread(target=receive_messages, daemon=True).start()
send_messages()
