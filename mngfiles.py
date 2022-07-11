import re
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
        nline = input()
        for line in range(int(nline)):
            line = input()  
            line = [ tag+'>' for tag in line.rsplit('>') ]
            for tag in line:
                if tag.find('/>') > 0:
                    print('Empty :', re.findall('<(\w+)', tag)[0])
                elif tag.find('/') > 0:
                    print('End :', re.findall('</(\w+)>', tag)[0])
                elif re.match('<(\w+)>', tag):
                    print('Start :', re.findall('<(\w+)>', tag)[0])
                elif tag != '>':
                    print('Start :', re.findall('<(\w+)', tag)[0])
                    for attr in tag.split():
                        if attr.find('=') > 0:
                            print('->', re.findall('(\w+)=', tag)[0],'>',re.findall('=\'(\w+)\'', tag)[0])
                        elif '<' not in attr:
                            print('->',attr,'> None')
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