import numpy as np

a = np.linspace(1,3,5)
# it will give five values between 1 and 3
print(a)

# max value
print(a.max())
# sum
print(a.sum())

# array
a = np.array([(1,2,3),(2,5,6)])
print(a.sum(axis=0))
print(a.sum(axis=1))
# square root
print(np.sqrt(a))
# standard deviation
print(np.std(a))
b = np.array([(3,5,6),(4,2,1)])
#addition
print(a+b)
#subtraction
print(a-b)
#multiplication
print(a*b)
#division
print(a/b)
#vertical stacking
print('Vertical stacking: ')
print(np.vstack((a,b)))
#horizontal stacking
print('horizontal stacking: ')
print(np.hstack((a,b)))
#in one column
print(a.ravel())