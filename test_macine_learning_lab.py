from mat import Mat
from vec import Vec
from vecutil import list2vec
from matutil import listlist2mat
from machine_learning_lab import signum
from machine_learning_lab import fraction_wrong


#v = signum(Vec({1,2,3},{1:2, 2:-1}))
#ref = Vec({1,2,3},{1:1,2:-1,3:1})
#print(v==ref)

A1 = listlist2mat([[10, 7, 11, 10, 14], [1, 1, 13, 3, 2], [6, 13, 3, 2, 6], [10, 10, 12, 1, 2], [2, 1, 5, 7, 10]])
b1 = list2vec([1, 1, -1, -1, 1])
A2 = Mat((set(range(97,123)),set(range(65,91))),{(x,y): 301-(7*((x-97)+26*(y-65))%761) for x in range(97,123) for y in range(65,91)})
b2 = Vec(A2.D[0], {x:(-1)**i for i, x in enumerate(sorted(A2.D[0]))})
print(fraction_wrong(A1, b1, Vec(A1.D[1], {})))
print('\n')
print(fraction_wrong(A1, b1, Vec(A1.D[1], {x:-2 for x in A1.D[1]})))
print('\n')
print(fraction_wrong(A1, b1, Vec(A1.D[1], {x: (-1)**i for i, x in enumerate(sorted(A1.D[1]))})))
print('\n')
print(fraction_wrong(A2, b2, Vec(A2.D[1], {})))
print('\n')
print(fraction_wrong(A2, b2, Vec(A2.D[1], {x:-2 for x in A2.D[1]})))
print('\n')
print(fraction_wrong(A2, b2, Vec(A2.D[1], {x: (-1)**i for i, x in enumerate(sorted(A2.D[1]))})))
print('\n')
