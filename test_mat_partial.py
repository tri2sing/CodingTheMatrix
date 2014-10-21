from mat import Mat
from vec import Vec
from GF2 import one


M = Mat((set(range(1000)), {'e',' '}), {(500, ' '): one, (255, 'e'): 0})
print(M[500, ' '])
print(M[500, 'e'])
print(M[255, 'e'])
print(M == Mat((set(range(1000)), {'e',' '}), {(500, ' '): one, (255, 'e'): 0}))
