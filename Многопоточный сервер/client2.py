import socket
sock = socket.socket()
sock.setblocking(1)
print('>Connecting client: ')
sock.connect(('127.0.0.1', 5050))
while True:
    msg = input('>Input message or "stop" to stop: ')
    data=msg.encode()
    sock.send(data)
    if msg == 'stop':
        break
    data = sock.recv(1024)
    print(f'>Message from server: ',data.decode())
print('>Stop server')
sock.close()


