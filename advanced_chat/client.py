import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox

HOST = "localhost"
PORT = 7000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# GUI Setup
window = tk.Tk()
window.title("Advanced Chat Application")
window.geometry("400x500")

chat_box = tk.Text(window)
chat_box.pack(pady=10)

entry = tk.Entry(window, width=30)
entry.pack(side=tk.LEFT, padx=10)

def send():
    msg = entry.get()
    if msg:
        client.send(msg.encode())
        entry.delete(0, tk.END)

send_btn = tk.Button(window, text="Send", command=send)
send_btn.pack(side=tk.RIGHT)

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            chat_box.insert(tk.END, msg + "\n")
        except:
            break

# Login Dialog
username = simpledialog.askstring("Login", "Username")
password = simpledialog.askstring("Login", "Password", show="*")

client.send(f"{username}:{password}".encode())
response = client.recv(1024).decode()

if response == "INVALID":
    messagebox.showerror("Error", "Invalid credentials")
    window.destroy()
elif response == "REGISTERED":
    messagebox.showinfo("Info", "New user registered")
elif response == "LOGIN_SUCCESS":
    messagebox.showinfo("Success", "Login successful")

threading.Thread(target=receive).start()

window.mainloop()
