class dictionaries:
    def numberwordlst(n):
        d = {}
        for x in range(n):
            word = input()
            d[word] = d.get(word, 0) + 1
        lvalues = list(d.values())
        print(len(d))
        print(*lvalues, sep=' ')
n = 4
dictionaries.numberwordlst(n)