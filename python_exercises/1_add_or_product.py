# Question 1: Accept two int values from the user and return their product. If the product is greater than 1000, then return their sum

def add_or_pro(a,b):
    if(a*b <1000):
        print('product of ',a,' and ',b,' is :',a*b)

    else:
        print('sum of ', a, ' and ', b, ' is :', a + b)

a = int(input('Enter first digit\t:'))
b = int(input('Enter second digit\t:'))

add_or_pro(a,b)