print("Bubble Sort")
A=[7,6,4,3,0]
n=len(A)
print("A=",A)
for p in range(1,n):
    print("Pass-",p)
    for i in range(0,n-p):
        if A[i]>A[i+1]:
            A[i],A[i+1]=A[i+1],A[i]
        print("\tA:",A)