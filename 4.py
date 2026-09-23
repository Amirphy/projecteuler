'''
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2 -digit numbers is
9009 = 91 × 99 .
Find the largest palindrome made from the product of two 3 -digit numbers.
'''

def is_palindrom(num):
	mun = 0
	while num > 0:
		divided= num % 10
		mun = mun * 10 + divided
		num //= 10
	return mun

def is_bigest(digit):
	start = 10 ** (digit -1)
	end = 10 ** digit
	largest = 0 
	for i in range(end, start - 1, -1):
		for j in range(i, start, -1):
			product = i * j
			if product <= largest:
				break
			if is_palindrom(product) == product :
				largest = product
	return largest

print(is_bigest(3))

# output is: 906609