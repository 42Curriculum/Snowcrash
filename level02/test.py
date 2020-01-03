import socket
import sys


HOST = ''
PORT = 6969
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(HOST, PORT)
sock.listen(0)

while true; do ~/./level10 /tmp/owo 127.0.0.1:w; done