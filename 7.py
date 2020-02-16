import numpy as np
import matplotlib.pyplot as plt
ar = np.array([1,2,3])

#exponent
print(np.exp(ar))
#natural log
print(np.log(ar))
#log 10
print(np.log10(ar))

#plot graph
x = np.arange(0,10,1)
y = np.log(x)
plt.plot(x,y)
plt.show()