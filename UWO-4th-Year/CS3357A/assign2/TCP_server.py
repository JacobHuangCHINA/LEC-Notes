
import socket
import datetime


def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)
    errorMesssage = 'Invalid request'
    print('Listening at', sock.getsockname())
    while True:
        print('Waiting to accept a new connection')
        sc, sockname = sock.accept()
        print('We have accepted a connection from', sockname)
        print('  Socket name:', sc.getsockname())
        print('  Socket peer:', sc.getpeername())
        message = sc.recv(1024)
        text = message.decode('ascii')
        if text == 'what is the current date and time?':
            text = 'Current time is: {0:%m-%d-%Y %H:%M:%S}'.format(datetime.datetime.now())
            sc.sendall(text.encode('ascii'))
        else:
            sc.sendall(errorMesssage.encode())

        sc.close()
        print('  Reply sent, socket closed')


if __name__ == '__main__':
    host = input("Enter the host: ")
    port = int(input("enter the port: "))
    server(host, port)
