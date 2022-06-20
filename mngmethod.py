from collections import defaultdict
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
Buildings.oceanview(heights)
#print(w1.count('x'))
#r = "".join(words)
#orderInd = dict()
#orderInd = { v : k for k,v in enumerate(i)}
#for k, v in enumerate(i):
#    orderInd[v] = k
#mapper = defaultdict(list) #if key not present, a list is associated to it
#list.extend([]) #add list to the end of list