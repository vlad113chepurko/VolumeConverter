import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("127.0.0.1", 7777))
socket.listen(1)

print("Server is running...")

conn, addr  = socket.accept()
print(f"Connection from: {addr}")



conn.close()
socket.close()