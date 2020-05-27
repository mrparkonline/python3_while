# Mr. Park
# 10.19.18
# Fibonacci Number

nthLocation = int(input("Enter a value of N: "))

fib_0 = 0
fib_1 = 1

if nthLocation == 0:
	print(0)
elif nthLocation == 1:
	print(1)
else:
	fib_n = 0 # initializing our variable
	counter = 2 # We already fib @ 0 and fib @ 1
	while counter <= nthLocation:
		fib_n = fib_1 + fib_0
		fib_0 = fib_1
		fib_1 = fib_n
		counter += 1
	# end our while loop

	print(fib_n)
