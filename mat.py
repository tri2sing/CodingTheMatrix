from vec import Vec

def identity(D, one):
    return Mat((D,D), {(d,d):1 for d in D})


def keys(d):
    return d.keys() if isinstance(d, dict) else range(len(d))


def value(d):
    return next(iter(d.values())) if isinstance(d, dict) else d[0]


def mat2rowdict(A):
    return {row:Vec(A.D[1], {col:A[row,col] for col in A.D[1]}) for row in A.D[0]}


def mat2coldict(A):
    return {col:Vec(A.D[0], {row:A[row,col] for row in A.D[0]}) for col in A.D[1]}


def coldict2mat(coldict):
        row_labels = value(coldict).D
        return Mat((row_labels, set(keys(coldict))), {(r,c):coldict[c][r] for c in keys(coldict) for r in row_labels})


def rowdict2mat(rowdict):
        col_labels = value(rowdict).D
        return Mat((set(keys(rowdict)), col_labels), {(r,c):rowdict[r][c] for r in keys(rowdict) for c in col_labels})


def getitem(M, k):
    "Returns the value of entry k in M.  The value of k should be a pair."
    assert k[0] in M.D[0] and k[1] in M.D[1]
    return M.f[k] if k in M.f else 0
 

def setitem(M, k, val):
    "Sets the element of v with label k to be val.  The value of k should be a pair"
    assert k[0] in M.D[0] and k[1] in M.D[1]
    M.f[k] = val

def add(A, B):
    "Returns the sum of A and B"
    assert A.D == B.D
    akeys = set(A.f)
    bkeys = set(B.f)
    both = akeys & bkeys
    aonly = akeys - both
    bonly = bkeys - both
    result = {}
    for k in both:
        result[k] = A.f[k]+B.f[k]
    for k in aonly:
        result[k] = A.f[k]
    for k in bonly:
        result[k] = B.f[k]
            
    return Mat(A.D, result)

def scalar_mul(M, alpha):
    "Returns the product of scalar alpha with M" 
    return Mat(M.D, {k:alpha*M[k] for k in M.f})

def equal(A, B):
    "Returns true iff A is equal to B"
    assert A.D == B.D
    union = set(A.f) | set (B.f)
    for k in union:
        aval = A.f[k] if k in A.f else 0  
        bval = B.f[k] if k in B.f else 0  
        if aval != bval:
            return False
    return True

def transpose(M):
    "Returns the transpose of M"
    m2rd = mat2rowdict (M)
    return coldict2mat(m2rd)

def vector_matrix_mul(v, M):
    "Returns the product of vector v and matrix M"
    assert M.D[0] == v.D
    m2cd = mat2coldict(M)
    return Vec(M.D[1], {k:v*m2cd[k] for k in m2cd})

def matrix_vector_mul(M, v):
    "Returns the product of matrix M and vector v"
    assert M.D[1] == v.D
    m2rd = mat2rowdict (M)
    return Vec(M.D[0], {k:m2rd[k]*v for k in m2rd})


def matrix_matrix_mul(A, B):
    "Returns the product of A and B"
    assert A.D[1] == B.D[0]
    rowsA = mat2rowdict (A)
    colsB = mat2coldict(B)
    return Mat((A.D[0], B.D[1]), {(i, j):rowsA[i]*colsB[j] for i in rowsA for j in colsB})

def toStr(M, rows=None, cols=None):
    "string representation for print()"
    if rows == None:
        try:
            rows = sorted(M.D[0])
        except TypeError:
            rows = sorted(M.D[0], key=hash)
    if cols == None:
        try:
            cols = sorted(M.D[1])
        except TypeError:
            cols = sorted(M.D[1], key=hash)
    separator = ' | '
    numdec = 3
    pre = 1+max([len(str(r)) for r in rows])
    colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
    s1 = ' '*(1+ pre + len(separator))
    s2 = ''.join(['{0:>{1}}'.format(c,colw[c]) for c in cols])
    s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
    s4 = ''.join(['{0:>{1}} {2}'.format(r, pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
    return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4



################################################################################

class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self,other):
        if Mat == type(other):
            return matrix_matrix_mul(self,other)
        elif Vec == type(other):
            return matrix_vector_mul(self,other)
        else:
            return scalar_mul(self,other)
            #this will only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __sub__(self, a,b):
        return a+(-b)

    __eq__ = equal

    __str__ = toStr
    
    def copy(self):
        return Mat(self.D, self.f.copy())


    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) +", " + str(self.f) + ")"
