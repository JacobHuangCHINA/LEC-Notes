
import socket
from datetime import datetime

MAX_BYTES = 65535


def client(host, port, request):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # send request to the server

    text = request
    while True:
        if text == 'what is the current date and time?':
            data = text.encode('ascii')
            sock.sendto(data, (host, port))
            break
        else:
            data = text.encode('ascii')
            sock.sendto(data, (host, port))
            #text = input("Enter your request: ")

    # recieve data from server
    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode('ascii')
    print('The server {} replied {!r}'.format(address, text))


if __name__ == '__main__':
    host = input("Enter the host: ")
    port = int(input("Enter the port: "))
    request = input("Enter your request: ")
    client(host, port, request)
