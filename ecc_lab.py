from vec import Vec
from mat import Mat
from bitutil import noise
from GF2 import one
import bitutil as butl

def listlist2mat(L):
    m,n = len(L), len(L[0])
    return Mat((set(range(m)),set(range(n))), {(r,c):L[r][c] for r in range(m) for c in range(n)})

def mat2coldict(A):
    return {col:Vec(A.D[0], {row:A[row,col] for row in A.D[0]}) for col in A.D[1]}

def keys(d):
    return d.keys() if isinstance(d, dict) else range(len(d))

def value(d):
    return next(iter(d.values())) if isinstance(d, dict) else d[0]

def coldict2mat(coldict):
        row_labels = value(coldict).D
        return Mat((row_labels, set(keys(coldict))), {(r,c):coldict[c][r] for c in keys(coldict) for r in row_labels})

## Task 1 part 1
""" Create an instance of Mat representing the generator matrix G. You can use
the procedure listlist2mat in the matutil module (be sure to import first).
Since we are working over GF (2), you should use the value one from the
GF2 module to represent 1"""
G = listlist2mat([[one, 0, one, one], [one, one, 0, one], [0, 0, 0, one], [one, one, one, 0], [0, 0, one, 0], [0, one, 0, 0], [one, 0, 0, 0]])

## Task 1 part 2
# Please write your answer as a list. Use one from GF2 and 0 as the elements.
encoding_1001 = [0, 0, one, one, 0, 0, one]

#v1001 = Vec({0, 1, 2, 3}, {0:one, 1:0, 2:0, 3:one})
#encoding_1001 = G*v1001


## Task 2
# Express your answer as an instance of the Mat class.
R = listlist2mat([[one, 0, one, one, 0, one, one], [one, one, 0, 0, one, 0, 0], [one, one, 0, one, one, 0, one], [one, one, one, 0, one, one, 0]])

# Task 2 took some doing.  Suppose G*p = c.  The we need to find R such that R*c = p.  
# using these two equations gives us the fact that RG = I (identity matrix).
# Did this manually one row at a time for R.  
#Chose some value of so that the vector (row from R) multiplied with matrix (G) gave the corresponding row of the identity matrix.

## Task 3
# Create an instance of Mat representing the check matrix H.
H = listlist2mat([[0, 0, 0, one, one, one, one], [0, one, one, 0, 0, one, one], [one, 0, one, 0, one, 0, one]])

## Task 4 part 1
def find_error(e):
    """
    Input: an error syndrome as an instance of Vec
    Output: the corresponding error vector e
    Examples:
        >>> find_error(Vec({0,1,2}, {0:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{3: one})
        >>> find_error(Vec({0,1,2}, {2:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{0: one})
        >>> find_error(Vec({0,1,2}, {1:one, 2:one}))
        Vec({0, 1, 2, 3, 4, 5, 6},{2: one})    
    """
    hcols = mat2coldict(H)
    return Vec({0, 1, 2, 3, 4, 5, 6}, {k:one for k in hcols if hcols[k] == e})
    
    
## Task 4 part 2
# Use the Vec class for your answers.
non_codeword = Vec({0,1,2,3,4,5,6}, {0: one, 1:0, 2:one, 3:one, 4:0, 5:one, 6:one})
error_vector = find_error (H*non_codeword)
code_word = non_codeword + error_vector
original = R*code_word # R * code_word


## Task 5
def find_error_matrix(S):
    """
    Input: a matrix S whose columns are error syndromes
    Output: a matrix whose cth column is the error corresponding to the cth column of S.
    Example:
        >>> S = listlist2mat([[0,one,one,one],[0,one,0,0],[0,0,0,one]])
        >>> find_error_matrix(S)
        Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 2): 0, (3, 2): one, (0, 0): 0, (4, 3): one, (3, 0): 0, (6, 0): 0, (2, 1): 0, (6, 2): 0, (2, 3): 0, (5, 1): one, (4, 2): 0, (1, 0): 0, (0, 3): 0, (4, 0): 0, (0, 1): 0, (3, 3): 0, (4, 1): 0, (6, 1): 0, (3, 1): 0, (1, 1): 0, (6, 3): 0, (2, 0): 0, (5, 0): 0, (2, 2): 0, (1, 3): 0, (5, 3): 0, (5, 2): 0, (0, 2): 0})
    """
    return coldict2mat ({key:find_error(val) for key, val in mat2coldict(S).items()})


## Task 6
s = "I'm trying to free your mind, Neo. But I can only show you the door. You’re the one that has to walk through it."
P = butl.bits2mat(butl.str2bits(s))

## Task 7
C = G*P
bits_before = len(butl.str2bits(s))
bits_after = len(butl.mat2bits(C))


## Ungraded Task
CTILDE = None

## Task 8
def correct(A):
    """
    Input: a matrix A each column of which differs from a codeword in at most one bit
    Output: a matrix whose columns are the corresponding valid codewords.
    Example:
        >>> A = Mat(({0,1,2,3,4,5,6}, {1,2,3}), {(0,3):one, (2, 1): one, (5, 2):one, (5,3):one, (0,2): one})
        >>> correct(A)
        Mat(({0, 1, 2, 3, 4, 5, 6}, {1, 2, 3}), {(0, 1): 0, (1, 2): 0, (3, 2): 0, (1, 3): 0, (3, 3): 0, (5, 2): one, (6, 1): 0, (3, 1): 0, (2, 1): 0, (0, 2): one, (6, 3): one, (4, 2): 0, (6, 2): one, (2, 3): 0, (4, 3): 0, (2, 2): 0, (5, 1): 0, (0, 3): one, (4, 1): 0, (1, 1): 0, (5, 3): one})
    """
    return A+find_error_matrix (H*A)
    pass
