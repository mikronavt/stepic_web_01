#simple server with one connection which sends response equals to request
__author__ = 'User'
import socket

server_host = '0.0.0.0'


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server_host, 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data: break
        print data.lower().find("close")
        if data.lower().find("close") >= 0:
            break
        conn.send(data)
    conn.close()
