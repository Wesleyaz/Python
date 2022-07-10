from ast import AnnAssign
from collections import Counter, defaultdict
from email.policy import default


order = 'QRBPVFDEIMwHNXSGYJULAZOTCK'
order = order.lower()
words = ['wesley','wycliffe','wycli','martha']

class AlienDict:
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

#AlienDict.issorted(order, words)
carac = dict()
carac2 = dict()
class Anagram:
    def isanagram(word1, word2):
        if len(word1) != len(word2):
            print('No')
            return False
        for i in range(len(word1)):
            carac2[word2[i]] = carac.get(word2[i], 0)
            carac[word1[i]] = carac.get(word1[i], 0)
        if carac != carac2:
            print('No')
            return False
        #if sorted(word1) != sorted(word2):
        #    print('No')
        #    return False
        else:
            print('Yes')
            return True
#w1, w2 = 'xxeasdw', 'exxdsaa'
#Anagram.isanagram(w1,w2)

class ValidParanthesis:
    def ispvalid(word):
        stack = []
        lw = list(word)
        for i in range(len(lw)):
            if lw[i] == '(':
                stack.append(i)
            elif lw[i] == ')':
                if stack:
                    stack.pop()
                else:
                    lw[i] = ''
        for j in stack:
            lw[j] = ''
        print(''.join(lw))
        return ''.join(lw)
word = 'asd))v((x(())9ck((hf)))s'
#ValidParanthesis.ispvalid(word)

class Intervals:
    def merge(intervals):
        intervals.sort()
        lmerged = [intervals[0]]
        for start,end in intervals[1:]:
            if lmerged[-1][1] >= start and end >= lmerged[-1][1]:
                lmerged[-1] = [lmerged[-1][0],end]
            elif lmerged[-1][0] <= start and lmerged[-1][1] > end:
                pass
            else:
                lmerged.append([start,end])
        print(lmerged)
        return lmerged
intervals = [[1,3],[2,6],[8,10],[15,18]]
#Intervals.merge(intervals)

class Btree:
    def lcolumns(root):
        mapper = defaultdict(list)
        def mapping(x,y,node):
            if not node:
                return
            mapping(x-1,y+1,node.left)
            mapping(x+1,y+1,node.right)
            mapper[(x,y)].append(node.val)
        mapping(0,0,root)
        output = []
        old = float('-inf')
        for k,v in sorted(mapper.items()):
            if k[0] == old:
                output[-1].extend(v)
            else:
                output[-1].append([])
            old = k[0]
        return output

class Buildings:
    def oceanview(heights):
        output = list()
        for i in reversed(range(len(heights))):
            if not output:
                output.append(i)
            elif heights[output[-1]] < heights[i]:
                output.append(i)
        print(sorted(output))
        return sorted(output)
heights = [4,3,2,1]
#Buildings.oceanview(heights)

class Power:
    def fast(x,n):
        y=x**n
        print(y)
    def cfor(x,n):
        y = x
        if n >= 0:
            for i in range(n-1):
                y = y * x
        else:
            for i in range(-n-1):
                y = y * x
            y = 1/y
        print(y)
        return y
x,n = 0.00001,2147483647
#Power.fast(x,n)

class Recurse:
    def fib(n):
        if n == 1:
            return 1
        return n + Recurse.fib(n-1)
    
    def pow(x,n):
        if x == 0 : return 0
        if n == 0 : return 1
        res = Recurse.pow(x,abs(n)//2)
        res = res * res
        if n % 2 != 0:
            res = res * x
        return res if n > 0 else 1/res

#res = Recurse.pow(2,29999999)
#print(res)

#print(w1.count('x'))
#r = "".join(words)
#orderInd = dict()
#orderInd = { v : k for k,v in enumerate(i)}
#for k, v in enumerate(i):
#    orderInd[v] = k
#mapper = defaultdict(list) #if key not present, a list is associated to it
#list.extend([]) #add list to the end of list



class Course:
    def anagram(s1,s2):
        if len(s1) != len(s2): return False
        ls2 = list(s2)
        for i in range(len(s1)):
            if s1[i] in ls2:
                ls2.pop(ls2.index(s1[i]))
            else:
                return False
        return True
        #Using sort, using counter
    
    def lfintpos(larr,target):
        if target not in larr:
            return [-1,-1]
        first = float('-inf')
        for x in range(len(larr)):
            print(larr[x])
            if larr[x] == target:
                if first < 0:
                    first = x
                last = x
        return [first,last]
    
    def klargelement(arr,k):
        if k > len(arr):
            return 'array smaller than', k
        return sorted(arr, reverse=True)[k-1]
        #removing the max elements
    
    def are_symetric(root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        return Course.are_symetric(root1.right, root2.left) and Course.are_symetric(root1.left, root2.right)
    def symetrictbtree(root):
        if root is None: return True
        return Course.are_symetric(root.left,root.right)

    def gasloop(gas,cost,start):
        glen = len(gas)
        remaining = 0
        i = start
        while i != start:
            remaining += gas[i] - cost[i]
            if n < 0:
                return False
            i = (i+1)%glen
        return True
    
    def validPalindromesub(s):
        l,r = 0,len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r - 1
        return False
s='aba'
print(Course.validPalindromesub(s))
s1,s2 = 'banana','aanbban'
#print(Course.anagram(s1,s2))

larr = [1,2,4,5,6,7,23,45,2,6,77668]
target = 1
#print(Course.lfintpos(larr,target))

#print(Course.klargelement(larr,target))