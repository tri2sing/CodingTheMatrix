from vec import Vec
from mat import Mat
import hw3


vin = Vec({0, 1, 2},{0: 1, 1: 2, 2:0})
vout = Vec({0, 1, 2},{0: 1, 1: 5, 2:6})
M1 = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 0): -1, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 3, (2, 0): 2, (2, 1): 2, (2, 2): 1})

lcmvm = hw3.lin_comb_mat_vec_mult(M1, vin)
print(lcmvm == vout)

dpmv = hw3.dot_product_mat_vec_mult (M1, vin)
print(dpmv == vout)

vin = Vec({0, 1, 2, 3},{0: 4, 1: 3, 2:2, 3:1})
vout = Vec({0, 1},{0: -40, 1: 80})
M2 = Mat(({0, 1, 2, 3}, {0, 1}), {(0, 0): -5, (0, 1): 10, (1, 0): -4, (1, 1): 8, (2, 0): -3, (2, 1): 6, (3, 0): -2, (3, 1): 4})
lcvmm = hw3.lin_comb_vec_mat_mult(vin, M2)
print(lcvmm == vout)

dpvm = hw3.dot_product_vec_mat_mult(vin, M2)
print (dpvm == vout)

d1 = {0, 1, 2, 3, 4}
d2 = {'a','b','c','d'}
d3 = {True, False}

D1 = (d1, d2)
D2 = (d2, d3)

M1 = Mat(D1, {(3, 'd'): 27, (1, 'c'): 26, (3, 'c'): 35, (3, 'a'): 20, (4, 'd'): 26, (1, 'd'): 5, (2, 'a'): 50, (2, 'b'): 11, (1, 'a'): 27, (2, 'c'): 34, (2, 'd'): 40, (4, 'a'): 33, (0, 'b'): 31}) 
M2 = Mat(D1, {(0, 'c'): 1, (3, 'd'): 2, (1, 'c'): 1, (0, 'a'): 1, (3, 'b'): 2, (1, 'b'): 2, (4, 'd'): 2, (1, 'd'): 2, (2, 'a'): 0, (2, 'b'): 2, (0, 'd'): 1, (2, 'c'): 2, (4, 'c'): 0, (4, 'a'): 1, (0, 'b'): 0})
M3 = Mat(D1, {(0, 'a'): 3, (4, 'd'): 4, (3, 'a'): 5, (2, 'a'): 5, (0, 'd'): 1, (1, 'a'): 3, (4, 'b'): 4, (2, 'c'): 3, (0, 'b'): 4, (3, 'b'): 5, (4, 'a'): 3, (2, 'd'): 3, (4, 'c'): 5})
M4 = Mat(D1, {(0, 'c'): 0, (3, 'c'): 2, (1, 'b'): 0, (4, 'd'): 2, (3, 'a'): 1, (1, 'd'): 1, (2, 'b'): 2, (2, 'a'): 2, (0, 'd'): 2, (1, 'a'): 0, (2, 'c'): 0, (4, 'c'): 0, (3, 'b'): 0, (3, 'd'): 1, (0, 'b'): 1})
V1 = Vec(d2, {'b': 12, 'c': 0, 'a': 2, 'd': 6})
V2 = Vec(d2, {'b': 19, 'c': 19, 'a': 19, 'd': 3})
V3 = Vec(d2, {'b': 18, 'c': 19})
matrices = [M1, M2, M3, M4]
vectors  = [V1, V2, V3]

func = hw3.lin_comb_mat_vec_mult
results = [func(M, V) for M in matrices for V in vectors]

func = hw3.dot_product_mat_vec_mult
results = [func(M, V) for M in matrices for V in vectors]
#for r in results:
#    print (str(r.D) + str(r.f))


N1 = Mat(D2, {('d', True): 2, ('b', False): 0, ('c', True): 0, ('a', True): 1, ('c', False): 0, ('d', False): 2, ('a', False): 1})
N2 = Mat(D2, {('b', False): 0, ('b', True): 0, ('c', True): 0, ('a', False): 0, ('a', True): 1, ('d', False): 0, ('d', True): 1})
N3 = Mat(D2, {('c', False): 0, ('b', False): 1, ('b', True): 1, ('d', False): 2, ('a', True): 2, ('d', True): 1, ('a', False): 1})
N4 = Mat(D2, {('b', True): 2, ('c', True): 2, ('a', False): 2, ('a', True): 1, ('c', False): 0, ('d', False): 1, ('d', True): 1})

Ms = [M1, M2, M3, M4]
Ns = [N1, N2, N3, N4]

func = hw3.Mv_mat_mat_mult
results = [func(M, N) for M in Ms for N in Ns]
#===============================================================================
# for r in results:
#     print (r.f.keys())
#     print (str(r.D) + str(r.f))
#     print('\n')
#===============================================================================

