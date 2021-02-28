# Question 5: Given a list of ints, return True if first and last number of a list is same


def CheckList(a):
    firstElement = a[0]
    lastElement = a[-1]
    if(firstElement == lastElement):
        return True
    else:
        return False


a=input('Give a coma separated list to check first and last element equality: \t')

Check_data = a.split(',')
if(len(Check_data) > 0):
    print('result is',CheckList(Check_data))


