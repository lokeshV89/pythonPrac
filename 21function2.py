# demo of function

user = 'lokesh'
def sayHello():
    global user
    user = 'krish'
    print('user = ',user)

sayHello()
print(user)