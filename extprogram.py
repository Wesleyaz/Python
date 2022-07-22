from ast import parse
from asyncio import tasks
from cgitb import html, text
from logging import root
import socket
from collections import Counter
import urllib
import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ETree
import json
import sqlite3
from html.parser import HTMLParser
import os
from pathlib import Path
class Webhttp: 
    def browserlib():
        hurl = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
        for line in hurl:
            print(line.decode().strip())

    def countWebTxt():
        wordfreq = urllib.request.urlopen('http://data.pr4e.org/romeo.txt').read()
        print(Counter(wordfreq.decode().split()))

    def getFromXML():
        xmldata = open('test.xml').read()
        datax = ETree.fromstring(xmldata)
        print('Name:', datax.find('name').text,'| Attr:', datax.find('email').get('hide'))
        lst = datax.findall('users/user')
        for user in lst:
            print('Name:', user.find('name').text,'|','Phone:',user.find('phone').text)

    def getFromJson():
        data = open('test.json').read()
        jdata = json.loads(data)
        #json.dumps(data,indent=4)
        print('Name:',jdata["name"],'| Phone',jdata["phone"]["number"])

    def getHtmlParse():
        class MYHTMLParser(HTMLParser):
            def __init__(self):
                self.startlst = list()
                self.startendlst =  list()
                super().__init__()
            def handle_starttag(self, tag, attrs):
                self.startlst.append(tag)
            def handle_endtag(self, tag): return
            def handle_startendtag(self, tag, attrs): return
        htmlfile = urllib.request.urlopen('http://data.pr4e.org/page1.htm').read()
        parser = MYHTMLParser()
        parser.feed(htmlfile.decode())
        print(parser.startlst)
        
    def importalfiles():
        #for filename in os.listdir():
        for path in Path('./').rglob('*.py'):
            print(path.name)
        #for root, subFolder, filename in os.walk('./'):
        #    print(os.path.join(root,subFolder,filename))

    def sqlplaying():
        conn = sqlite3.connect('email.sqlite')
        cur = conn.cursor()
        email = "a@hotmail.com"
        cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
        row = cur.fetchone()
        conn.commit()

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

Webhttp.importalfiles()
#Webhttp.getHtmlParse()
#Webhttp.httpconnect()
#Webhttp.browserlib()
#Webhttp.countwebtxt()
#Webhttp.getfromxml()
#Webhttp.getfromjson()