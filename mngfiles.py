fname = input('Enter file name: ')
try:
    xfile = open(fname)
except:
    print('File does not exist')
    quit()

counts = dict()
for line in xfile:
    #line = line.rsplit()
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



#Count Number of From
#count = 0
#for line in xfile:
#    line = line.rstrip()
#    if line.startswith('From:'):
#        count += 1
#print(count)
#find /var/www/html/ -type f|d -exec chmod 755 {} \; ||| nginx -t