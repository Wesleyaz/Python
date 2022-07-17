from cgitb import text
import socket
from collections import Counter
import urllib
import urllib.request, urllib.error, urllib.parse
from weakref import WeakSet
import xml.etree.ElementTree as ETree
class Webhttp:
    def browserlib():
        hurl = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
        for line in hurl:
            print(line.decode().strip())
    def countwebtxt():
        wordfreq = urllib.request.urlopen('http://data.pr4e.org/romeo.txt').read()
        print(Counter(wordfreq.decode().split()))
    def getfromxml():
        xmldata = open('test.xml').read()
        datax = ETree.fromstring(xmldata)
        print('Name:', datax.find('name').text,'| Attr:', datax.find('email').get('hide'))
        lst = datax.findall('users/user')
        for user in lst:
            print('Name:', user.find('name').text,'|','Phone:',user.find('phone').text)
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
#Webhttp.countwebtxt()
Webhttp.getfromxml()