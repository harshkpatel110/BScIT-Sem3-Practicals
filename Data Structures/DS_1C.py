print("Selection Sort")
A=[50,75,65,45,35]
n=len(A)
print("A =",A)
for i in range(n-1):
    print("Pass -",i+1)
    min_elt=A[i]
    flag=0
    for j in range(i+1,n):
        if A[j]<min_elt:
            min_elt=A[j]
            pos=j
            flag=1
    if flag==1:
        A[i],A[pos]=A[pos],A[i]
    print("\tA :",A)