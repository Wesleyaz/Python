import socket
import urllib.request, urllib.error, urllib.parse
class Webhttp:
    def browserlib():
        hurl = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
        for line in hurl:
            print(line.decode().strip())
    def httpreqconnect():
        mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mysock.connect(('data.pr4e.org', 80))
        cmd = 'GET http:/data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
        mysock.send(cmd)
        while True:
            data = mysock.recv(512)
            if (len(data) < 1):
                break
            print(data.decode())
        mysock.close()

#Webhttp.httpconnect()
Webhttp.browserlib()