## In this problem we are summing all numbers that are multiples of 3 or 5 up to 1000

sum = 0

for i in range (1000):
	if (i % 3 == 0 or i % 5 == 0):
		sum += i
		
print("The sum is " + str(sum))
