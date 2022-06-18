
order = 'QRBPVFDEIMwHNXSGYJULAZOTCK'
order = order.lower()
words = ['wesley','wycliffe','wycli','martha']

class Solution:
    def issorted(order, words):
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            print(w1, w2)
            for j in range(len(w1)):
                if j == len(w2):
                    print('less letters')
                    return "False"
                if w1[j] != w2[j]:
                    print(order.index(w2[j]))
                    print(order.index(w1[j]))
                    if order.index(w2[j]) < order.index(w1[j]):
                        print('chegou')
                        return "False"
                    break
        return "True"

Solution.issorted(order, words)



#orderInd = dict()
#orderInd = { v : k for k,v in enumerate(i)}
#
#for k, v in enumerate(i):
#    orderInd[v] = k
#
#print(orderInd)
#
#a = 'Wesley'
#
#print(len(a))
#print(range(len(a)))