import numpy as np
a = np.array([(1,2,3),(4,5,6)])

c = np.array([(7,8,9),(5,8,9)])

# TO GET DIMENTIONS OF ARRAY
print(a.ndim)
#to get datatype
print(a.dtype)
# to get size of an array
print(a.size)
# linespacing print an array with 10 values between 1 to 5
b = np.linspace(1,5,10)
print(b)
# array slicing
print(a[0,2]) #indexing 0 row 2 element is 3
print(a[0:,1]) # 0: includes all rows and give there 1 column value
# to get min, max,sum,prod in array
print(a.max())
print(a.min())
print(a.sum())
print(a.prod())

# rows are axis 1 and colmn are axis 0
print(a.sum(axis=0)) # 1+4  2+5  3+6
print(a.sum(axis=1)) #  1+2+3   4+5+6

# to print squareroot of each element in array
print(np.sqrt(a))

# to print standard deviation of each element in array
print(np.std(a))

# sum of two array
print(a+c)
print(a-c)
print(a*c)
print(a/c)
print(np.vstack((a,c))) #virtical concat
print(np.hstack((a,c))) # horigontal concat
print(np.ravel(a))  #converting into 1d



