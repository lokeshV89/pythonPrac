import numpy as np
# single dimentional array
a = np.array([1,2,3])
# multi dimentional array
b = np.array([(1,2,3),(4,5,6)])
print(a)
print(b)
# create a array of 1000 number
d = np.arange(1000)
print(d)
print(d.itemsize)
# to get a tupple having array dimensions
print(a.shape)
print(b.shape)

# to reshap a array

c = b.reshape(3,2)
print(c)