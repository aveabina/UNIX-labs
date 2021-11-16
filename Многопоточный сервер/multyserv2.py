import socket
import sys
import threading
def MultyServer(conn, addr):
    while True:
        print('>Data received from client')
        try:
            data = conn.recv(1024)
            print('>Message from client ', addr, ': ', data.decode)
            print('>Message received to client')
            conn.send(data)
        except (ConnectionResetError, ConnectionAbortedError):
            print('>Break connecting with client')
            raise
sys.tracebacklimit = 0
sock = socket.socket()
print('>Start server')
sock.bind(('', 5050))
print('>Start listen port')
sock.listen(0)
while True:
    conn, addr = sock.accept()
    print(">Connecting client: ",addr)
    multy=threading.Thread(target = MultyServer, args = (conn, addr), daemon = True)
    multy.start()
print('>Stop server work')


