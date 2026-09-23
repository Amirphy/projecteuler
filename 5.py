"""
Problem 5
2520
is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
"""

def divid(num, upto):
    for i in range(1, upto):
        if num % i != 0:
            return False
    return True

n = 1
while not divid(n, 20):
    n += 1
    # comment: 
# end while
print(n)


#output: 232792560