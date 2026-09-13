def armstrong(num):
    temp=num
    total=0
    power=len(str(num))
    while temp>0:
        digit=temp%10
        total+=digit**power
        temp//=10
    if total==num:
        return True
    else:
        return False
def palindrome(value):
    text=str(value)
    return text==text[::-1]
num=int(input("Enter a number: "))
if armstrong(num):
    print(num, "is an Armstrong Number.")
else:
    print(num, "is not an Armstrong Number.")
if palindrome(num):
    print(num, "is a Palindrome.")
else:
    print(num, "is not a Palindrome.")