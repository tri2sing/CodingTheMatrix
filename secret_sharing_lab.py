# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from independence import is_independent
from vecutil import list2vec
from itertools import combinations



## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    while True:
        u = list2vec([randGF2() for _ in range(6)])
        if a0*u == s and b0*u == t: return u

## Problem 2
# Give each vector as a Vec instance

def randVec(): return list2vec([randGF2() for _ in range(6)])
  
# There has to be a more efficient way to do this one  
def independent_vecs():
        while True:
            L = [randVec() for _ in range(8)]
            T = [(a0, b0), (L[0], L[1]), (L[2], L[3]), (L[4], L[5]), (L[6], L[7])]
            if all(is_independent(list(sum(x,()))) for x in combinations(T,3)): return L
        
secret_a0 = a0
secret_b0 = b0
L = independent_vecs()
secret_a1 = L[0]
secret_b1 = L[1]
secret_a2 = L[2]
secret_b2 = L[3]
secret_a3 = L[4]
secret_b3 = L[5]
secret_a4 = L[6]
secret_b4 = L[7]

