def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
num=int(input("Enter a number to find its factorial: "))
if num>=0:
    print(f"Factorial of {num} is {factorial(num)}.")
else:
    print("Factorial is not defined for negative numbers.")