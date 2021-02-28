print("Enter the range of dimension to print pattern")
x = int(input("Enter length value : "))
y = int(input("Enter width value : "))
for j in range(x):
    for i in range(y):
        print("# ",end="")
        i+=1
    j += 1    
    print()

