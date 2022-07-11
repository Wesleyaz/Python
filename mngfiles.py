import re
from html.parser import HTMLParser
class files:
    def countnumwords():
        file = open(input()).read()
        scount = file.count(" ")
        print(scount+1)
    def wordsfreq():
        hfile = open(input())
        counts = dict()
        for line in hfile:
            words = line.rsplit()
            for word in words:
                counts[word] = counts.get(word, 0) + 1
        lst = list()
        for key,val in counts.items():
            invertedtup = (val, key)
            lst.append(invertedtup)
        lst = sorted(lst, reverse=True)
        for val,key in lst[:10]:
            print(key,val)
    def printtagtypes():
        class MyHTMLParser(HTMLParser):
            def handle_starttag(self, tag, attrs):
                print("Start :", tag)
                if attrs:
                    for attr in attrs:
                        print('->',attr[0],'>',attr[1])
            def handle_endtag(self, tag):
                print("End   :", tag)
            def handle_startendtag(self, tag, attrs):
                print("Empty :", tag)
                if attrs:
                    for attr in attrs:
                        print('->',attr[0],'>',attr[1])
        
        nline = input()
        parser = MyHTMLParser()
        
        for line in range(int(nline)):
            line = input()
            parser.feed(line)
#files.printtagtypes()
#files.countnumwords()
#files.wordsfreq()

#Count Number of From
#count = 0
#for line in xfile:
#    line = line.rstrip()
#    if line.startswith('From:'):
#        count += 1
#print(count)
#find /var/www/html/ -type f|d -exec chmod 755 {} \; ||| nginx -t