import socket

ip = "127.0.0.1"
port = 8008
message = "[+]client: Hello Server!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.sendto(bytes(message, "utf-8"), (ip, port))