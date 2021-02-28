x = 0

while x <= 5:
    print(x)
    x = x+1

#using break statment
x=0
while x<= 6:
    print(x)
    if(x==3):
        break

    x += 1

#using continue statment
x=0
while x<= 6:

    x += 1
    if(x==3):
        continue
    print(x)
