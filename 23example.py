def count(l):
    odd=0
    even=0
    for i in l:
        if i%2==0:
            even += 1
        else:
            odd += 1
    return odd,even

list = [2,4,6,9,7,21,22,45,47,63,70,80,95,97]

odd,even =  count(list)

print("Even : {} and Odd : {} in list".format(even,odd) )