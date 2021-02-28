'''
    We can use * to unpack the list so that all elements of it can be passed as different parameters.
'''

myList = [1,2,3,4]

def myFun(a,b,c,d):
    print(a+b+c+d)

# the above function takes for variables and prints there sum

# if we pass above list as parameter it will give error so we have to unpack the list and pass to unpack use *

myFun(*myList)

