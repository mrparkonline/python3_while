# Factorial Calculator

# input
num = int(input("Enter a value: "))
factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print(factorial)
