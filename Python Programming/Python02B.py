num=int(input("Enter the number: "))
sum=0
num=abs(num)
while num>0:
    sum+=num%10
    num=num//10
print(f"Sum of all digits of this number is {sum}.")