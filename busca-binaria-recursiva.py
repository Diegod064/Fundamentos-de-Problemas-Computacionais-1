import math

ent = [int(ent) for ent in input().split()] #5 1 2 3 4 5 6 7

l = []  #1 2 3 4 5 6 7

for i in range(1, len(ent)):
    l.append(ent[i])

e = ent[0] #5
i = math.floor(len(l)/2)
c = 0  #contador das funcoes

def f(i):
    global c
    if len(l) == 0:
        return c
    if e == l[i]:
        c += 1
        return c
    if e < l[i]:
        del l[i:]
        c += 1
        return f(math.floor(len(l)/2))
    if e > l[i]:
        del l[:i + 1]
        c += 1
        return f(math.floor(len(l)/2))

f(i)

print(c)

