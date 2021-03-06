from vec import Vec
from mat import Mat
from vecutil import list2vec
from matutil import listlist2mat
from GF2 import one
import hw5


S = [list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]]
B = [list2vec(v) for v in [[1,1,0],[0,1,1],[1,0,1]]]
for (z, w) in hw5.morph(S, B):
    print("injecting ", str(z.D) + str(z.f))
    print("ejecting ", str(w.D) + str(w.f))
    print()


#injecting  {0, 1, 2}{0: 1, 1: 1, 2: 0}
#ejecting  {0, 1, 2}{0: 1, 1: 0, 2: 0}

#injecting  {0, 1, 2}{0: 0, 1: 1, 2: 1}
#ejecting  {0, 1, 2}{0: 0, 1: 1, 2: 0}

#injecting  {0, 1, 2}{0: 1, 1: 0, 2: 1}
#ejecting  {0, 1, 2}{0: 0, 1: 0, 2: 1}


# 
# [(Vec({0, 1, 2},{0: 1, 1: 1, 2: 0}),     Vec({0, 1, 2},{0: 1, 1: 0, 2: 0})), 
# (Vec({0, 1, 2},{0: 0, 1: 1, 2: 1}),     Vec({0, 1, 2},{0: 0, 1: 1, 2: 0})), 
# (Vec({0, 1, 2},{0: 1, 1: 0, 2: 1}),     Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}))
# ]


L = [Vec({0, 1, 2},{0: 1, 1: 0, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 1})]
print(hw5.my_is_independent(L))
#False
print(hw5.my_is_independent(L[:2]))
#True
print(hw5.my_is_independent(L[:3]))
#True
print(hw5.my_is_independent(L[1:4]))
#True
print(hw5.my_is_independent(L[0:4]))
#False
print(hw5.my_is_independent(L[2:]))
#False
print(hw5.my_is_independent(L[2:5]))
#False


a0 = Vec({'a','b','c','d'}, {'a':1})
a1 = Vec({'a','b','c','d'}, {'b':1})
a2 = Vec({'a','b','c','d'}, {'c':1})
a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
L = hw5.subset_basis([a0,a1,a2,a3]) 
V = [Vec({'c', 'b', 'a', 'd'},{'a': 1}), Vec({'c', 'b', 'a', 'd'},{'b': 1}), Vec({'c', 'b', 'a', 'd'},{'c': 1})]
print('\nSubset Basis')
print (L==V)
for l in L:
    print(l.D)
    print(l.f)
    print()


U_basis = [Vec({0, 1, 2, 3, 4, 5},{0: 2, 1: 1, 2: 0, 3: 0, 4: 6, 5: 0}), Vec({0, 1, 2, 3, 4, 5},{0: 11, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0}), Vec({0, 1, 2, 3, 4, 5},{0: 3, 1: 1.5, 2: 0, 3: 0, 4: 7.5, 5: 0})]
V_basis = [Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 7, 3: 0, 4: 0, 5: 1}), Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 15, 3: 0, 4: 0, 5: 2})]
w = Vec({0, 1, 2, 3, 4, 5},{0: 2, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0})
refM = (Vec({0, 1, 2, 3, 4, 5},{0: 2.0, 1: 4.999999999999972, 2: 0.0, 3: 0.0, 4: 1.0, 5: 0.0}), Vec({0, 1, 2, 3, 4, 5},{0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}))
retV = hw5.direct_sum_decompose(U_basis, V_basis, w)
print('\ndirect sum decompose')
print(type(retV))
print (refM == retV)

print('\nis invertible')
M = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 0, (1, 2): 1, (3, 2): 0, (0, 0): 1, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2, (2, 1): 0, (0, 2): 1, (2, 0): 0, (1, 3): 0, (2, 3): 1, (2, 2): 3, (1, 0): 0, (0, 3): 0})
print(hw5.is_invertible(M))

A = Mat(({0, 1}, {0, 1, 2}), {(0, 1): 2, (1, 2): 1, (0, 0): 1, (1, 0): 3, (0, 2): 3, (1, 1): 1})
print(hw5.is_invertible(A))
B = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 0, (1, 2): 1, (3, 2): 0, (0, 0): 1, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2, (2, 1): 0, (0, 2): 1, (2, 0): 0, (1, 3): 0, (2, 3): 1, (2, 2): 3, (1, 0): 0, (0, 3): 0})
print(hw5.is_invertible(B))
C = Mat(({0, 1, 2}, {0, 1}), {(0, 1): 0, (2, 0): 2, (0, 0): 1, (1, 0): 0, (1, 1): 1, (2, 1): 1})
print(hw5.is_invertible(C))
D = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 5, (1, 2): 2, (0, 0): 1, (2, 0): 4, (1, 0): 2, (2, 2): 7, (0, 2): 8, (2, 1): 6, (1, 1): 5})
print(hw5.is_invertible(D))
E = Mat(({0, 1, 2, 3, 4}, {0, 1, 2, 3, 4}), {(1, 2): 7, (3, 2): 7, (0, 0): 3, (3, 0): 1, (0, 4): 3, (1, 4): 2, (1, 3): 4, (2, 3): 0, (2, 1): 56, (2, 4): 5, (4, 2): 6, (1, 0): 2, (0, 3): 7, (4, 0): 2, (0, 1): 5, (3, 3): 4, (4, 1): 4, (3, 1): 23, (4, 4): 5, (0, 2): 7, (2, 0): 2, (4, 3): 8, (2, 2): 9, (3, 4): 2, (1, 1): 4})
print(hw5.is_invertible(E))


print('\nfind inverse')
M = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): one, (1, 2): 0, (0, 0): 0, (2, 0): 0, (1, 0): one, (2, 2): one, (0, 2): 0, (2, 1): 0, (1, 1): 0})
N = hw5.find_matrix_inverse(M) 
NRef = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): one, (2, 0): 0, (0, 0): 0, (2, 2): one, (1, 0): one, (1, 2): 0, (1, 1): 0, (2, 1): 0, (0, 2): 0})
print(N == NRef)

print('\ntriangular inverse')
A = listlist2mat([[1, .5, .2, 4],[0, 1, .3, .9],[0,0,1,.1],[0,0,0,1]])
N = hw5.find_triangular_matrix_inverse(A) 
NRef = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): -0.5, (1, 2): -0.3, (3, 2): 0.0, (0, 0): 1.0, (3, 3): 1.0, (3, 0): 0.0, (3, 1): 0.0, (2, 1): 0.0, (0, 2): -0.05000000000000002, (2, 0): 0.0, (1, 3): -0.87, (2, 3): -0.1, (2, 2): 1.0, (1, 0): 0.0, (0, 3): -3.545, (1, 1): 1.0})
print(N == NRef)


A = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 2, (1, 2): 3, (3, 2): 0, (0, 0): 1, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2, (2, 1): 0, (0, 2): 3, (2, 0): 0, (1, 3): 4, (2, 3): 4, (2, 2): 3, (1, 0): 0, (0, 3): 4})
Ainv = hw5.find_triangular_matrix_inverse(A)
B = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 4, (1, 2): 5, (3, 2): 0, (0, 0): 7, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2, (2, 1): 0, (0, 2): 2, (2, 0): 0, (1, 3): 6, (2, 3): 4, (2, 2): 7, (1, 0): 0, (0, 3): 5})
Binv = hw5.find_triangular_matrix_inverse(B)
B = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 3, (1, 2): 6, (3, 2): 0, (0, 0): 6, (3, 3): 2345, (3, 0): 0, (3, 1): 0, (1, 1): 4, (2, 1): 0, (0, 2): 4, (2, 0): 0, (1, 3): 23, (2, 3): 2, (2, 2): 6, (1, 0): 0, (0, 3): 8})
Cinv = hw5.find_triangular_matrix_inverse(C)

