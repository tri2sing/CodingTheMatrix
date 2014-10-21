from hw7 import QR_solve
from mat import coldict2mat
from mat import Mat
from orthonormalization import aug_orthonormalize
from QR import factor
from vec import Vec
from vecutil import list2vec

print('Augmented Orthonormalize')
L = [list2vec(v) for v in [[4,3,1,2],[8,9,-5,-5],[10,1,-1,5]]]
print(coldict2mat(L))
Qlist, Rlist = aug_orthonormalize(L)
print(coldict2mat(Qlist))
print(coldict2mat(Rlist))
print((coldict2mat(Qlist)*coldict2mat(Rlist)))

print('QR Solve')

A=Mat(({'a','b','c'},{'A','B'}), {('a','A'):-1, ('a','B'):2, ('b','A'):5, ('b','B'):3,('c','A'):1, ('c','B'):-2})
print(A)
Q, R = factor(A)
print(Q)
print(R)
b = Vec({'a','b','c'}, {'a':1,'b':-1})
x = QR_solve(A,b)
print(x)
residual = A.transpose()*(b-A*x)
print(residual)
