import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
link = "GET https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0/ HTTP/2.0\r\n\r\n"
default_link = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'
mysock.connect(('data.pr4e.org', 80))
cmd = default_link.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data)< 1:
        break
    print(data.decode(), end='')

mysock.close()