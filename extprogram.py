import socket
from collections import Counter
import urllib
import urllib.request, urllib.error, urllib.parse
class Webhttp:
    def browserlib():
        hurl = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
        for line in hurl:
            print(line.decode().strip())
    def countwebtxt():
        hurl = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
        wordfreq = dict()
        for line in hurl:
            words = line.decode().split()
            for word in words:
                wordfreq[word] = wordfreq.get(word, 0) + 1
        lst = [ (v,k) for k,v in wordfreq.items() ]
        lst = sorted(lst, reverse=True)
        for v,k in lst[:10]:
            print(k,v)
        #print(wordfreq)

    def httpreqconnect():
        mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mysock.connect(('data.pr4e.org', 80))
        cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
        mysock.send(cmd)
        while True:
            data = mysock.recv(512)
            if (len(data) < 1):
                break
            print(data.decode())
        mysock.close()

#Webhttp.httpconnect()
#Webhttp.browserlib()
Webhttp.countwebtxt()