from hw6 import is_echelon
from hw6 import echelon_solve
from vec import Vec
from GF2 import one



ans = is_echelon([[2, 1, 0], [0, -4, 0], [0, 0, 1]])
print(ans)
ans = is_echelon([[2, 1, 0], [-4, 0, 0], [0, 0, 1]])
print(ans)
ans = is_echelon([[2, 1, 0], [0, 3, 0], [1, 0, 1]])
print(ans)
ans = is_echelon([[1, 1, 1, 1, 1], [0, 2, 0, 1, 3], [0, 0, 0, 5, 3]])
print(ans)


print('\nFrom submit_hw6.py')
M1 = [[0,0,0],[0,0,0],[0,0,0]]
M2 = [[1,0,0],[0,1,0],[0,1,0]]
M3 = [[0]*4,[1]*4]
M4 = [[1,0,0,0,0,0,0,0], [0,1,1,1,1,1,1,1],[0,0,1,1,1,0,1,0], [0,0,0,0,0,1,1,0]]
M5 = [[1]]
M6 = [[0]]
results = [is_echelon(M) for M in [M1, M2, M3, M4, M5, M6]]
print(results)


print('\nEchelon Solve')
D = {'A','B','C','D','E'}
U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
b_list = [one,0,one]
cols = ['A', 'B', 'C', 'D', 'E']
res = echelon_solve(U_rows, cols, b_list)
print (res == Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one}))

D = {'A','B','C','D','E'}
U_rows = [Vec(D, {'A':one, 'C':one, 'D':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one, 'E':one}), Vec(D,{'E':one})] 
b_list = [one,0,one, one]
cols = ['A', 'B', 'C', 'D', 'E']
res = echelon_solve(U_rows, cols, b_list)
print(res == Vec({'B', 'C', 'A', 'D', 'E'},{'A': one, 'B': one, 'C': 0, 'D': 0, 'E': one}))

D = {'A','B','C','D','E'}
U_rows = [Vec(D, {'A':one, 'B':one, 'D':one}), Vec(D, {'B':one, 'D':one, 'E':one}), Vec(D,{'C':one, 'E':one}), Vec(D,{'A':0, 'B':0, 'C':0, 'D':0, 'E':0})] 
b_list = [one, 0, one, 0]
cols = ['A', 'B', 'C', 'D', 'E']
res = echelon_solve(U_rows, cols, b_list)
print(res == Vec({'B', 'C', 'A', 'D', 'E'},{'A': one, 'B': 0, 'C': one, 'D': 0, 'E': 0}))
