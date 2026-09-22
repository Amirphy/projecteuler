#The prime factors of 13195 are 5, 7, 13 and 29

def prime(num):
    if num<2:
        return None
    for i in range(2,int(num** 0.5) + 1):
        if num % i == 0:
            return None
    return num


def check(num):
    largest = None
    for i in range(2, int(num**0.5)):
        if num % i == 0 and prime(i):
            largest = i
    return largest

a= check(600851475143)
print(a)
        
# here i use ai for have a patent to solve int(num**0.5) to make it more optimized
