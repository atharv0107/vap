"""
a=[1,2,3]
b=[4,5,6]
print(a+b)


#load all the classes and function fron numpy

import numpy
from numpy import array   #only load array from numpy
import numpy as np        #standard alternative for numpy

a=np.array([1,2,3])
b=np.array([4,5,6])


print(a+b)

#2-D array

matrix=array([[1,2],[3,4],[5,6]])
print(matrix.ndim)                      #Array attributes
print(matrix.shape)
print(matrix.size)
print(matrix.dtype)
print(np.zeros((3,3)))
print(np.ones((2,2)))
print(np.arange((1,10)))
print(np.arange((1,10,2)))
print(np.arange((0,10,2)))



#
arr=np.array([10,20,30,40])
print(arr[2])
print(np.int64(30))
print(arr[-1])
print(arr[:3])
print(arr[::-1])


#
mat=array(([1,2,3],[4,5,6]))
print(arr.dtype)
print(mat[0,1])
"""
import numpy as np

arr=np.array([1,2,3])
print(arr.dtype)
arr=arr.astype(np.float32)
print(arr.dtype)
print(arr.nbytes)

