A=[0,0,0,0,0,0,0,0,0,0]
print("A", A)
m=10
for i in range (5):
    n=int(input("Enter any number: "))
    r=n%m
    p=0
    print(r)
    while A[r]!=0:
        print("Collision")
        p+=1
        r=(n%m+p)%m
    A[r]=n
    print("A", A)
