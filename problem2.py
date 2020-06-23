##In this problem, we are summing the even numbers of the Fibonacci sequence up to 4,000,000

sum = 0;
num1 = 0;
num2 = 1;

while num2 < 4e6:
	num1, num2 = num2, num1+num2
	if num1 % 2 == 0:
		sum += num1
		
print("The sum is: " + str(sum))

