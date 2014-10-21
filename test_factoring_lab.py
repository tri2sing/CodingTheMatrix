from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod
from factoring_lab import find_candidates
from factoring_lab import find_a_and_b
from factoring_lab import smallest_nontrivial_divisor_of_2461799993978700679 as sntd
from echelon import transformation_rows
from factoring_support import prod
from math import sqrt

from vec import Vec
from GF2 import one

import echelon

def root_method(N):
    a = intsqrt(N)
    for i in range (a+1, N):
        d = i*i - N
        if d < 0: 
            continue
        else: 
            b = sqrt(d)
            #print(str(i) + ':' + str(b))
        if b%1 == 0: 
            return int(i-b)

    return None



N = 367160330145890434494322103
a = 67469780066325164
b = 9429601150488992
d = a*a - b*b
#print(d)
#print(d%N == 0)
g = gcd(a-b, N)
#print(g)
#print (N%g == 0)

r = 99083208324108213
s = 54982011313211212
t = 23239982309329329
a = r*s
b = s*t
d = gcd(a, b)
#print(a%d == 0)
#print(b%d == 0)
#print(d > s)


R,L = find_candidates(2419, primes(32))
#R = result[0]
#L = result[1]
for i in range(len(L)):
    print('%s, %s' % (R[i], L[i].f))

M = transformation_rows(L)
print(M)
v = M[-1]
print(v.f)

a, b = find_a_and_b(v, R, 2419)
print(a)
print(b)

print(sntd)