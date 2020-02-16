import numpy as np
import time
import sys

a = np.array([(1,3,5),(2,5,3)])
#check dimensions
print(a.ndim)
#check bytesize
print(a.itemsize)
#check datatype
print(a.dtype)
#size of array
print(a.size)
#shape of array
print(a.shape)
#reshape converting row to column
a = np.array([(1,2,3,4),(3,5,6,7)])
a = a.reshape(4,2)
print(a)

#slicing
a = np.array([(1,2,3,4),(4,5,6,7),(7,8,9,10)])
#print(a[0,2])
#print(a[0:,2])
#print(a[0:2,3])
print(a[0:,3])