from GF2 import one
from vec import Vec
from vec import scalar_mul
import itertools


## Problem 1
    
D = {'a','b','c'}
v0 = Vec(D, {})
v1 = Vec(D, {'a': 1})
v2 = Vec(D, {'a': 0, 'b': 1})
v3 = Vec(D, {        'b': 2})
v4 = Vec(D, {'a': 10, 'b': 10})

def vec_select(veclist, k): 
    return [Vec(v.D, v.f) for v in veclist if v[k]==0]

def vec_sum(veclist, D):
    return sum(veclist, Vec(D, {}))

def vec_select_sum(veclist, k, D): 
    return vec_sum(vec_select(veclist, k), D)
 
def scale_vecs(vecdict):
    return [scalar_mul(vecdict[k], 1.0/k) for k in vecdict]
 
def GF2_span(D, L):
    result = [Vec(D, {})]
    if not L:
        return result
    
    indices = [k for k in range(len(L))]
    for num in range (1,len(indices)+1):
        for tuples in itertools.combinations(indices, num):
            vectorslist = [L[i] for i in list(tuples)]
            combination = vec_sum(vectorslist, D)
            result.append(combination)
    return result
      
print(vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})])
print(vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11}))
print(vec_sum([], D) == v0)
print(vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3}))

v5 = Vec({1,2,3}, {2: 9})
v6 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
print(scale_vecs({3: v5, 5: v6}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})])

D = {'a', 'b', 'c'}
L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
GF2Combs = GF2_span(D, L)
print (len(GF2Combs) == 4)
print (Vec(D, {}) in GF2Combs)
print (Vec(D, {'b': one}) in GF2Combs)
print (Vec(D, {'a':one, 'c':one}) in GF2Combs)
print (Vec(D, {x:one for x in D}) in GF2Combs)

