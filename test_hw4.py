import hw4
from mat import Mat
from mat import coldict2mat
from mat import rowdict2mat
from solver import solve
from vec import Vec

a0 = Vec({'a','b','c','d'}, {'a':1})
a1 = Vec({'a','b','c','d'}, {'b':1})
a2 = Vec({'a','b','c','d'}, {'c':1})

l = [a0, a1, a2]
m = coldict2mat (l)
print(m.D)
print(m.f)
print('\n')

u = Vec({0,1,2}, {0:2, 1:4, 2:6})
print(u.D)
print(u.f)
print('\n')

v = m*u

print(v.D)
print(v.f)
print('\n')

v1 = Vec({'a','b','c','d'}, {'a':3, 'c':-2})

u2 = solve(m, v1)
print(u2.D)
print(u2.f)
print('\n')

a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})

print('Testing is_superfluous')
print('\n')
l1 = [a0, a1, a2, a3]
b = hw4.is_superfluous(l1, 3)
print (b)
b = hw4.is_superfluous(l1, 0)
print (b)
b = hw4.is_superfluous(l1, 1)
print (b)

z = Vec({0, 1, 2}, {})
print(z.D)
print(z.f)
print('\n')

vlist = [Vec({0, 1, 2},{0: 1, 1: 0, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 0})]
b = hw4.is_independent(vlist)
print (b)
b = hw4.is_independent(vlist[:3])
print (b)
hw4.is_independent(vlist[:2])
print (b)
b = hw4.is_independent(vlist[1:4])
print (b)
b = hw4.is_independent(vlist[2:5])
print (b)
b = hw4.is_independent(vlist[2:6])
print (b)
b = hw4.is_independent(vlist[1:3])
print (b)
b = hw4.is_independent(vlist[5:])
print (b)
print('\n')



L1 = hw4.superset_basis([a0, a3], [a0, a1, a2]) 
L2 =  [Vec({'a', 'c', 'b', 'd'},{'a': 1}), Vec({'a', 'c', 'b', 'd'},{'b':1}),Vec({'a', 'c', 'b', 'd'},{'c': 1})]
print('Superset Basis')
for v in L1:
    print(v.D)
    print(v.f)
print(L1 == L2)
print('\n')
# L2 is from the sample in HW4, but that is not the only answer
# in comparing lists for equality the order of items in the two lists should be the same
L3 =  [Vec({'a', 'c', 'b', 'd'},{'a': 1}), Vec({'a', 'c', 'b', 'd'},{'a':1, 'c':3}), Vec({'a', 'c', 'b', 'd'},{'b':1})]
print(L1 == L3)
print('\n')

L3 = [Vec({'a', 'c', 'b', 'd'},{'a': 1}), Vec({'a', 'c', 'b', 'd'},{'b':1})]
L4= [Vec({'a', 'c', 'b', 'd'},{'a': 1}), Vec({'a', 'c', 'b', 'd'},{'b':1})]
print (L3 == L4)


def list2vec(L):
    return Vec(set(range(len(L))), {k:L[k] for k in range(len(L))})


S = [list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]]
A = [list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]]
z = list2vec([0,2,1,1])
v5 = hw4.exchange(S, A, z) 
v6 = Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 1, 3: 0})
print('exchange')
print(v5.D)
print(v5.f)
print(v5 == v6)
print('\n')





