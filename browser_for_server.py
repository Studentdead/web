import socket


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 9000))
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
value = b""
while True:
    data = mysock.recv(512)
    value += data
    if len(data) < 1:
        break
    #print(data.decode(), end='')

headers, body = value.decode().split('\r\n\r\n', 1)
# print(headers)
for line in headers.split('\r\n')[1:]:
    print(line)
mysock.close()