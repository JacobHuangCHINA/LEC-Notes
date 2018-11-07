import socket
from datetime import datetime

MAX_BYTES = 65535


def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        if text == 'what is the current data and time?':
            print('The client at {} says {!r}'.format(address, text))
            text = 'Current Date and Time - {0:%m/%d/%Y %H:%M:%S}'.format(datetime.now())
            data = text.encode('ascii')
            sock.sendto(data, address)
        else:
            print('Invalid request from client.')
            text = 'Invalid request from client.'
            data = text.encode('ascii')
            sock.sendto(data, address)


if __name__ == '__main__':
    host = input("Enter the host: ")
    port = int(input("enter the port: "))
    server(host, port)
