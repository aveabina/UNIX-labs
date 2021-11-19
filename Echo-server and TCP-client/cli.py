import socket
import random

while True:
    port = input('Input port to connect client: ')
    if port.isdigit():
        if 1024 <= int(port) <= 65535:
            port = int(port)
            with open("ports.txt", "r+") as pfile:
                pfile.write(str(port))
            break
        else:
            print('Port should be between 1024 and 65535!')
    else:
        print('!Invalid value!')

while True:
    flag=False
    host=input('Input host: ')
    phost=host.split('.')
    for i in range(len(phost)):
            if  len(phost) == 4:
                if phost[i].isdigit():
                    if 0 <= int(phost[i]) <= 255:
                        flag = True
                    else:
                        flag = False
                        break
                else:
                    flag=False
                    break
            else:
                break
    if flag==True:
        break

    print('!Invalid input!')
file=open('cli_data.txt', 'a+')
cli=0
with open('cli_data.txt','r') as f:
    for line in f:
        list_words = line.split()
        if host in line:
            name = list_words[-2]
            passwd=list_words[-1]
            cli = 1
if cli!=1:
    name = input('Input name: ')
    passwd = input('Input password: ')
    file.write(host + ' ')
    file.write(name + ' ')
    file.write(passwd+ ' ')
file.close()
while True:
    if_passwd=input('Enter password: ')
    if if_passwd!=passwd:
        print('!Invalid password!')
    else:
        break
while True:
    with open("ports.txt", "r") as pfile:
        lines = pfile.readlines()
        port = int(lines[-1])
    with socket.socket() as sock:
        print('Welcome,'+name+'!')
        sock.connect((host, port))
        print("Received data from client: ")
        while True:
            msg = input('Input message, "end" to exit: ')
            if msg == 'end':
                break
            sock.send(msg.encode())
            print("Send data to server")
            data = sock.recv(1024)
            print('Received data from server:', repr(data))
    print("Break connection with server")
    break
pfile=open('ports.txt','w')
pfile.close()
