n = int(input("How many terms of Fibonacci series do you want to print?"))
if n>0:
    a,b=0,1
    print("Fibonacci series:")
    for i in range(n):
        print(a)
        a,b=b,a+b
else:
    print("Invalid input. Please enter a positive integer.")