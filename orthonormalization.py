from math import sqrt
from mat import coldict2mat
from mat import rowdict2mat
from mat import mat2coldict
from mat import mat2rowdict
from mat import transpose
from orthogonalization import orthogonalize
from orthogonalization import aug_orthogonalize
from vec import Vec

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    orths = orthogonalize(L)
    norms = [sqrt(v*v) for v in orths]
    return [(1/norms[i])*vec for i, vec in enumerate(orths)]


def adjust(vector, mult):
    f = {k: vector.f[k]*mult for k in vector.f}
    return Vec(vector.D, f)

def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    vstarlist, tcols = aug_orthogonalize(L)
    sigmas = [sqrt(v*v) for v in vstarlist]
    qlist = orthonormalize(vstarlist)
    T = coldict2mat(tcols)  
    trows = mat2rowdict(T)
    rrows = [adjust(trows[k], sigmas[k]) for k in trows]
    rdict = mat2coldict(rowdict2mat(rrows))
    rlist = [rdict[k] for k in rdict]
    return qlist, rlist
