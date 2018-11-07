import socket
import datetime


def client(host, port, request):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('Client has been assigned socket name', sock.getsockname())
    text = request
    while True:
        data = text.encode('ascii')
        if text == 'what is the current date and time?':
            sock.sendall(data)
            break
        else:
            sock.sendall(data)
            text = input("Enter your request: ")
    reply = sock.recv(1024)
    print('The server said', repr(reply))
    sock.close()


if __name__ == '__main__':
    host = input("Enter the host: ")
    port = int(input("Enter the port: "))
    request = input("Enter the request: ")
    client(host, port, request)
