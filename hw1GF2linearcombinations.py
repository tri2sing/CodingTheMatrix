import itertools
from GF2 import one

#===============================================================================
# a = [one, one, 0, 0, 0, 0, 0]
# b = [0, one, one, 0, 0, 0, 0]
# c = [0, 0, one, one, 0, 0, 0]
# d = [0, 0, 0, one, one, 0, 0]
# e = [0, 0, 0, 0, one, one, 0]
# f = [0, 0, 0, 0, 0, one, one]
#===============================================================================

print ('\nPart1\n')

arr = [
    [one, one, 0, 0, 0, 0, 0],
    [0, one, one, 0, 0, 0, 0],
    [0, 0, one, one, 0, 0, 0],
    [0, 0, 0, one, one, 0, 0],
    [0, 0, 0, 0, one, one, 0],
    [0, 0, 0, 0, 0, one, one]
    ]

tgt1 = [0, 0, one, 0, 0, one, 0]
tgt2 = [0, one, 0, 0, 0, one, 0]

for a in arr:
    print(a)
print('\n') 
   
l = [k for k in range(len(arr))]
print(l)
print('\n') 

#===============================================================================
# allcombs = [[list(x) for x in itertools.combinations(l, i)] for i in range (len(l), 1, -1)]
# for comb in allcombs:
#     print (comb)
# print('\n') 
#===============================================================================

for num in range (len(l), 1, -1):
    for combs in itertools.combinations(l, num):
        indices = list (combs)
        #print (indices)
        sub = [arr[i] for i in indices]
        zipped = zip(*sub)
        total = [sum(a) for a in zipped]
        if (total == tgt1):
            print (str(indices) + 'sum matches' + str(tgt1))
        if (total == tgt2):
            print (str(indices) + 'sum matches' + str(tgt2))
        #print (total)


print ('\nPart2\n')

arr = [
    [one, one, one, 0, 0, 0, 0],
    [0, one, one, one, 0, 0, 0],
    [0, 0, one, one, one, 0, 0],
    [0, 0, 0, one, one, one, 0],
    [0, 0, 0, 0, one, one, one],
    [0, 0, 0, 0, 0, one, one]
    ]

tgt1 = [0, 0, one, 0, 0, one, 0]
tgt2 = [0, one, 0, 0, 0, one, 0]

for a in arr:
    print(a)
print('\n') 
   
l = [k for k in range(len(arr))]
print(l)
print('\n') 

#===============================================================================
# allcombs = [[list(x) for x in itertools.combinations(l, i)] for i in range (len(l), 1, -1)]
# for comb in allcombs:
#     print (comb)
# print('\n') 
#===============================================================================

for num in range (len(l), 1, -1):
    for combs in itertools.combinations(l, num):
        indices = list (combs)
        #print (indices)
        sub = [arr[i] for i in indices]
        zipped = zip(*sub)
        total = [sum(a) for a in zipped]
        if (total == tgt1):
            print (str(indices) + 'sum matches' + str(tgt1))
        if (total == tgt2):
            print (str(indices) + 'sum matches' + str(tgt2))
        