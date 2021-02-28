#Question 3: Accept string from the user and display only those characters which are present at an even index

def fun(a):

    if(a.isdigit()):
        print("input is not string")

    else:
        for x in range(len(a)):
            if(x%2 == 0):
                print('index[',x,']',a[x])

val =  input("enter any string to get is even char\t")

print('even chars in string : ',val,' as following ')
fun(val)

