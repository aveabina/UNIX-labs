import os
import socket
import threading
import sys
import csv
from time import sleep
logfile=open('log.txt','a+')
logfile.close()
clients = []
logins = []
def Send(msg):
    for client in clients:
        client.send(msg)
def Receive(client):
    while True:
        try:
            msg = client.recv(1024)
            data=msg.decode('utf-8')
            data=data.split(':')
            with open('msgs.csv', mode="a+", encoding='ascii', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow((data))
            Send(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = logins[index]
            logins.remove(name)
            break
host = '127.0.0.1'
port = 5050
print('>Start server')
fi = open('log.txt', 'a')
fi.write('>Start server'+'\n')
fi.close()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()
def MultyServer():
    while True:
        com = input('>Press "Enter" to continue or input "stop" to stop:')
        if com == 'stop':
            for client in clients:
                msg = b'>Stop server'
                client.send(msg)
            break
        ip, addr = sock.accept()
        print('>Client: ' + str(addr))
        ip.send('login'.encode('utf-8'))
        login = ip.recv(1024).decode('utf-8')
        logins.append(login)
        clients.append(ip)
        fi = open('log.txt', 'a+')
        fi.write('>Client: ' + str(addr) + '\n')
        fi.write('>Login: ' + login + '\n')
        fi.close()
        print('>Login: ' + login)
        Send("{} added to chat".format(login).encode('utf-8'))
        threading.Thread(target=Receive, args=(ip,)).start()
MultyServer()
print('Server not working')
print('Input command: '
 '\n "ShowLog" to show log-file'
 '\n "ClearLog" to clear log-file'
 '\n "ClearCli" to clear clients list'
 '\n  "Stop" to stop')
while True:
    command = input('>')
    if command == 'ShowLog':
        if os.stat("log.txt").st_size == 0:
            print('!File is empty!')
        else:
            file = open('log.txt', 'r')
            fi = file.read()
            print(fi)
            file.close()
    if command == 'ClearLog':
        f = open('log.txt', 'w')
        f.close()
    if command == 'ClearCli':
        f = open("msgs.csv", "w")
        f.truncate()
        f.close()
        print('>Clients list cleared')
    if command=='Stop':
        break
fi = open('log.txt', 'a')
fi.write('Server not working'+'\n')
fi.close()
