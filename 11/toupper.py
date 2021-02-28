import socket
import sys

sock = socket.socket()
sock.bind(("", 8765))
sock.listen(1)
while True:
    con, addr = sock.accept()
    while True:
        c = con.recv(1024)
        print(c)
        r = c.decode().upper().encode()
        print(r)
        con.sendall(r)
