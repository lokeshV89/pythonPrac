f = open("demo.txt","r")  #this could be both .doc and .text files
f1 = open("demo.txt","a")
print(f.read())
f1.write("now the file has one more line")
f2= open("demo.txt","r")
print(f2.read())
print(f.read())