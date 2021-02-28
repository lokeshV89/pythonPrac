#python strings
str = " hello workd this is, string example and its ops.... "

print (str)             # Prints complete string
print (str[0])          # Prints first character of the string
print (str[2:5])        # Prints characters starting from 3rd to 5th
print (str[2:])         # Prints string starting from 3rd character
print (str * 2)         # Prints string two times
print (str + "TEST")    # Prints concatenated string
print (len(str))        # prints length of string
print (str.title())     # capatalise the first characteres
print (str.lower())     # prints string to lower
print (str.upper())     # prints string to upper
print (str.strip())     # remove whitespace from front and end
print (str.count('this')) # count the occurence of substring
print (str.isalpha())   # return boolean value if all are fro a-z of A-Z
print (str.isdigit)
print (str.replace("h","..."))  # replace h
print (str.split(","))  #split a string
print (str.find('w'))  #finds the first occurrence of a substring in another string. If not found, the method returns -1
print ("t" in str)      # returns true or false for the exixtence of a characters
#print command line string input

print("Enter your name")

x =  input()    #stores the input value in a variable

print("hello", x)

print ("add two number")
print ("Enter first numbers")

l = input()

print ("Enter second number")

m = input()
print(l+m)
print(int(l)+int(m))


