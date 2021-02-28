def person(name,**data):
    print ("name")

    for i,j in data.items():
        print(i,j)
person('lokesh',age=29,city='beawar',mob=7734859877)