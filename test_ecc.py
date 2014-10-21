from vec import Vec
from mat import Mat
from GF2 import one
import ecc_lab as ecl
import matutil as util

v1001 = Vec({0, 1, 2, 3}, {0:one, 1:0, 2:0, 3:one})
encoding_1001 = ecl.G*v1001
print(type(encoding_1001))
print(encoding_1001.D)
print(encoding_1001.f)
mat_enc = Mat ((), {})

prod=ecl.R*ecl.G
print(prod.D)
print(prod.f)
print ('\n')

prod=ecl.H*ecl.G
print(prod.D)
print(prod.f)
print ('\n')


v1 = ecl.find_error(Vec({0,1,2}, {0:one}))
print (v1 == Vec({0, 1, 2, 3, 4, 5, 6},{3: one}))
v2 = ecl.find_error(Vec({0,1,2}, {2:one}))
print (v2 == Vec({0, 1, 2, 3, 4, 5, 6},{0: one}))
v3 = ecl.find_error(Vec({0,1,2}, {1:one, 2:one}))
print (v3 == Vec({0, 1, 2, 3, 4, 5, 6},{2: one}))    
print ('\n')

S = util.listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
em = ecl.find_error_matrix(S)
tm = Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 2): 0, (3, 2): one, (0, 0): 0, (4, 3): one, (3, 0): 0, (6, 0): 0, (2, 1): 0, (6, 2): 0, (2, 3): 0, (5, 1): one, (4, 2): 0, (1, 0): 0, (0, 3): 0, (4, 0): 0, (0, 1): 0, (3, 3): 0, (4, 1): 0, (6, 1): 0, (3, 1): 0, (1, 1): 0, (6, 3): 0, (2, 0): 0, (5, 0): 0, (2, 2): 0, (1, 3): 0, (5, 3): 0, (5, 2): 0, (0, 2): 0})
print (em == tm)
print ('\n')






