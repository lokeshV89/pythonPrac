import re

str = "hello world! its flooding all over india, due to heavy rain its almost 29 days"

# find all chars between a to m

x = re.findall("[a-m]",str)

print(x)

# Find all digit characters:

x = re.findall("\d", str)
print(x)

# Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..y", str)
print(x)

# Check if the string starts with 'hello':

x = re.findall("^hello", str)
if (x):
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

# Check if the string ends with 'world':

x = re.findall("days$", str)
if (x):
  print("Yes, the string ends with 'days'")
else:
  print("No match")


# Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("aix*", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

# Check if the string contains "ai" followed by 1 or more "x" characters:

x = re.findall("aix+", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


# Check if the string contains "a" followed by exactly two "l" characters:

x = re.findall("al{2}", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|days", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


# /s is the escape sequence for white space

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())
# it returns none if no match found
str = "The rain in Spain"
x = re.search("Portugal", str)
print(x)


# split

str = "The rain in Spain"
x = re.split("\s", str)
print(x)

# it splits only at 1st occ

x = re.split("\s", str, 1)
print(x)

# sub replaces chars in string

x = re.sub("\s", "9", str)
print(x)

x = re.sub("a", "9", str)
print(x)

# replaces first 2 occ
x = re.sub("\s", "9", str, 2)
print(x)
