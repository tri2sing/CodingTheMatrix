from vec import Vec
from GF2 import one

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod
from math import sqrt
import echelon


## Task 1
def int2GF2(i):
    '''
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    '''
    if (i%2 == 0): return 0
    else: return one
    

## Task 2
def make_Vec(primeset, factors):
    '''
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    '''
    return Vec(primeset, {factors[i][0]:int2GF2(factors[i][1]) for i in range(len(factors))})

## Task 3
def find_candidates(N, primeset):
    '''
    Input:
        - N: an int to factor
        - primeset: a set of primes

    Output:
        - a list [roots, rowlist]
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    '''
    roots = []
    rowlist = []
    isr = intsqrt(N)
    
    count = 0
    k = 2
    while count < len(primeset) + 1:
        x = isr + k
        facts = dumb_factor (x*x - N, primeset)
        if facts != []:
            count += 1
            roots.append(x)
            rowlist.append(make_Vec(primeset, facts))
        k += 1
    
    return (roots, rowlist)

## Task 4
def find_a_and_b(v, roots, N):
    '''
    Input: 
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    '''
    alist = [roots[k] for k in v.f if v.f[k] == one]
    a = prod(alist)
    clist = [x*x-N for x in alist]
    c = prod(clist)
    b = intsqrt(c)
    if b*b == c: return (a, b)
    else: return (None, None)

## Task 5

def find_smallest_nontrivial():
    N = 2461799993978700679
    primelist = primes(1000)
    roots, rowlist = find_candidates (N, primelist)
    M = echelon.transformation_rows (rowlist, sorted(primelist, reverse=True))
    num = len(M)
    for i in range(num-1, -1, -1):
        a, b = find_a_and_b(M[i], roots, N)
        if a is not None:
            g = gcd (a-b, N)
            if g != 1: return g 


smallest_nontrivial_divisor_of_2461799993978700679 = find_smallest_nontrivial()
