import numpy as np

d = np.array([[1, 2], [3, 4]])
print(type(d), d, d.shape)
e = np.array([[5, 6], [7, 8]])
print(type(e), e, e.shape)
f = np.concatenate((d, e))
print(type(f), f, f.shape)
