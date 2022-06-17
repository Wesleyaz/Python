from contextlib import nullcontext
from http.client import MOVED_PERMANENTLY

inp=input('What the number? ')
try:
    numb=int(inp)
except:
    print ("Insira um valor válido")
    exit()

def comparenumb(number):
    if number < 5:
        return 'Less than 5'
    if number > 5:
        return 'Greater than 5'
    else:
        return 'Equal to 5'

listnum = list()

while True:
    print(numb, comparenumb(numb))
    listnum.append(numb)
    if numb < 1:
        for numbers in listnum:
            print(numbers)
        for letter in inp:
            print(letter)
        if '5' in inp:
            print('Found 5')
        print('Length:', len(listnum), '\n'+'Biggest:'.lower(), max(listnum))
        break
    numb -= 1

#dictionaries
purse = dict()
purse['money'] = 10
purse['tissues'] = 5

print(purse, purse['money'], purse.get('money', 17))

#TUPLES: Eficient, imutalbes
#Can compare: (1, 0) < (2,0) = True | (c,b) < (b,a) = False
 