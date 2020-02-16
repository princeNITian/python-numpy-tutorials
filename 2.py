import numpy as np

import time

import sys

S = range(1000)
print(S)
print(sys.getsizeof(5)*len(S))
D = np.arange(1000)
print(D.size*D.itemsize)