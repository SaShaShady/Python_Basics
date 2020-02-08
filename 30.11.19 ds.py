'''numpy is faster than list.
 numpy is as good as list but only takes homogenous elements..list is heterogenous
 no of columns is no of dimensions
 METHODS OF NUMPY
 1.ZEROS
 2.OMES
 3.EYE
 4.DIAG
 5.RAND
 6.RARDINT
 7.RANDM
import numpy as np
l=[[10,20],[2,5],[3,3]]
l1=np.array(l)
print(l1)
print(l1.dtype)
print(l1.shape)'''

print("*************************************************************************")

import numpy as np
import random
l2=[5,5]
l3=np.zeros(l2)
print(l3)

print("*****************************************************************************")

s=[2,5,6]
s1=np.ones(s)
print(s1)

s2=np.eye(3,3,1)
print(s2)

print("******************************************************************************")

s3=np.diag((2,3,5)) """diag elements"""
print(s3)

print("******************************************************************************")

w=np.random.randn(2,10) """col and rows"""
print(w)

w=np.random.rand(2,10) """col and rows"""
print(w)

w=np.random.randint(2,10,(4,5)) """first value second value no of rows and col"""
print(w)

s=np.array([1,2],[3,4],[0,-1])
s.sort(axis=0)
print(s)