import socket
import threading
def Receive():
    while True:
        try:
            msg= sock.recv(1024).decode('utf-8')
            if msg == 'login':
                sock.send(login.encode('utf-8'))
            else:
                print(msg)
        except:
            print(">Stop connecting with client")
            sock.close()
            break
def Send():
    while True:
        data=input('>')
        msg=login+':'+data
        sock.send(msg.encode('utf-8'))
        if data=='stop':
            print('>Stop connecting with client')
            sock.close()
            break
login = input("Input login: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 5050))
threading.Thread(target=Receive).start()
threading.Thread(target=Send).start()
