import socket

# Address of Server
Host = '127.0.0.1'
port=1337

# Create a socket object
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((Host, port))
while True:
    send = input("Enter a message: ")
    send="Client: "+send+"\n"
    socket.send(send.encode())
    if send == 'bye':
        print("Connection closed")
        socket.close()
    else:
        recieve = socket.recv(1024)
        print(recieve.decode())
        if recieve.decode() == 'bye':
            print("Connection closed")
            socket.close()
