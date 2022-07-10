#sent = input('Enter setence: ')
'''
file = input('Enter file: ')
if not file:
    file = "tfile.txt"
hfile = open(file)

for line in hfile:
    words = line.split()
    counts = { word:words.count(word) for word in words}



#counts = { word:sent.count(word) for word in sent }
print(counts)
'''

file = open(input()).read()
scount = file.count(" ")
print(scount+1)