
def function1():
    print("hello world")

def function2(name,age):
    print("myname is "+name+"myage is"+age)
    print("myname is ",name,"myage is",age)

def function3(name = "lokesh",age= "27"):  #this is function with default if we not pass any primeter it will take its default parimiter
    print("my name is "+name+"and age is "+age)

def function4(*name):  # * is used to use flexible number of aguments
    for x in name:
        print("this is "+x)
def function5(x,y): # return
    return x+y

a =function5(2,3)
b=function5(1,7)

print("sum of 2 and 3 is ",a,"sum of 1 and 7 is ",b)

function1()
function2("lokesh","29")
function3()
function3("ram","15")
function4("rel","black","end","1","india")
