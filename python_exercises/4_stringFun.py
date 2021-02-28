#Question 4: Given a string and an int n, remove characters from a string starting from zero up to n and return a new string

def steFun(a,b):
    print(a[b:])

a = input('Enter the string\n :')
b = int(input('enter the number after which char are required\n :'))

if(len(a)<b):
    print('digit value is greater then total length')

else:
    steFun(a,b)


