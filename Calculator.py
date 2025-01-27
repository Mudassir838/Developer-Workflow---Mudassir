def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def divide_three_numbers(x, y, z):
    if y == 0 or z == 0:
        return "Error: Division by zero is not allowed."
    return x / y / z

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5.Divide Three Number")

choice = int(input("Enter your choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    result = add(num1, num2)
elif choice == 2:
    result = sub(num1, num2)
elif choice == 3:
    result = mul(num1, num2)
elif choice == 4:
    result = div(num1, num2)
elif choice == 6:
    nums = list(map(float, input("Enter 3 numbers separated by space: ").split()))
    if len(nums) != 3:
        result = "Error: Please enter exactly 3 numbers."
    else:
        result = divide_three_numbers(*nums)
else:
    result = "Error: Invalid choice!"

print("Result:", result)