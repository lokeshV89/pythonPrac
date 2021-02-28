import json as j
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = j.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y)
