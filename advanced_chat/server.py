import socket
import threading
import hashlib

HOST = "localhost"
PORT = 7000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
users = {}

# Load users
def load_users():
    try:
        with open("users.txt", "r") as f:
            for line in f:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        open("users.txt", "w").close()

def save_user(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")

def encrypt(msg):
    return msg.encode()

def decrypt(msg):
    return msg.decode()

def broadcast(message, client):
    for c in clients:
        if c != client:
            c.send(encrypt(message))

def handle_client(client):
    try:
        credentials = decrypt(client.recv(1024)).split(":")
        username, password = credentials[0], credentials[1]

        hashed = hashlib.sha256(password.encode()).hexdigest()

        if username not in users:
            users[username] = hashed
            save_user(username, hashed)
            client.send(encrypt("REGISTERED"))
        elif users[username] != hashed:
            client.send(encrypt("INVALID"))
            client.close()
            return
        else:
            client.send(encrypt("LOGIN_SUCCESS"))

        clients.append(client)
        broadcast(f"{username} joined the chat", client)

        while True:
            msg = decrypt(client.recv(1024))
            broadcast(f"{username}: {msg}", client)

    except:
        clients.remove(client)
        client.close()

print("Advanced Chat Server Started...")
load_users()

while True:
    client, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
