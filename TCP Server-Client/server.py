import socket

# Address of a Host

Host = '127.0.0.1'
port = 1337  # this should be a int

# Create a socket object
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
socket.bind((Host, port))
while True:
    # listen for connections
    print('Listening for connections...')
    socket.listen()
    # accept connections
    connection, address = accept = socket.accept()
    # accept the connection
    print('Connection accepted from', accept[1])
    while True:
        recieve = connection.recv(1024)
        print('client: '+recieve.decode())
        if recieve.decode() == 'bye':
            print("Connection closed")
            socket.close()
        else:
            send = input("Enter a message: ")
            send="Server: "+send+"\n"
            connection.send(send.encode())
            if send == 'bye':
                print("Connection closed")
                socket.close()
