#simple multithread server which sends response equals to request
__author__ = 'User'
import socket, threading


server_host = '0.0.0.0'


def connection(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data: break
        if data.lower().find("bue") >= 0:
            break
        conn.send(data)
    conn.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server_host, 5050))
s.listen(10)
while True:
    conn, addr = s.accept()
    server_thread = threading.Thread(target=connection, args=(conn, addr))
    server_thread.start()
