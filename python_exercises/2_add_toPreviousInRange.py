# Question 2: Given a range of numbers. Iterate from o^th number to the end number and print the sum of the current number and previous number

def add_toPrev(a):
    previousNum = 0
    for i in range(a):
        sum = previousNum + i
        print(sum)
        previousNum = i



add_toPrev(9)

