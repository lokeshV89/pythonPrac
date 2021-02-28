def fac(x):
    for i in range(1,x):
        f=x*i
    return f

x = int(input("Enter the number to get factorial : "))
ans = fac(x)
print(ans)
