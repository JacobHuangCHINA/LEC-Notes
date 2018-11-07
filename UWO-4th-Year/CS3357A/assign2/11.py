import argparse
import socket
import datatime


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind('127.0.0.1', port)
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        try:
            data, address = recvfrom(1024)
            text = data.decode('ascii')
            print('The client at {} says {!r}'.format(address, text))
            text = 'Your data was {} bytes long'.format(len(data))
            data = text.encode('ascii')
            sock.sendto(data, address)
