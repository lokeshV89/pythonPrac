'''
There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members. Not necessary to declare in ()
             be declared without brackets
    Set is a collection which is unordered and unindexed. No duplicate members.
    Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


'''


num = [1,2,3,4,5,6,7] #list
thistuple = ("apple", "banana", "cherry") #tupple
thisset = {"apple", "banana", "cherry"} #set
thisdict = {
    'name':'lokesh',
    'age':'31',
    'occupation':'study'
}

#loop through lists
for x in num:
    print(x)
#check if item exists in  list
if x in num:
    print("yes")
#print length of list
print(len(num))
#print dictionary
print(thisdict)
#access individual items for dectionary
print(thisdict['name'])
#change incividuyal keys
thisdict["age"] = 32
# loop access disc keys
print(thisdict.keys())
#access values of desc
print(thisdict.values())
#to loop through dics keys and values
for x,y in thisdict.items():
    print(x,y)

#nested disctionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily['child3']['name'])


# to copy a list use copy method
num_new = num.copy()
# join two lists using + symbol
print(num+num_new)
print(num_new)
print (num[0])
num.append(9)
print(num)
num.insert(2,11)
print(num)


