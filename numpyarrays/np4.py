import numpy as np
a = np.array(np.arange(10))
b = np.array([2,3,5,7,11,15])
c = np.concatenate((a, b))
d = np.array([[1, 2], [3, 4]])
e = np.array([[5, 6], [7, 8]])
f = np.concatenate((d, e))
print("Dimension Array {} : {} ".format(a,a.ndim))
print("Dimension Array {} : {} ".format(f,f.ndim))
