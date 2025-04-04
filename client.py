import socket
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("450x320")
root.config(bg="#1d1d1d")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello tkinter!", background="#1d1d1d", font='Arial 13').grid(column=0, row=0)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("127.0.0.1", 7777))


print("Client is running...")

resp = socket.recv(1024).decode()
socket.send(resp.encode())

root.mainloop()
socket.close()