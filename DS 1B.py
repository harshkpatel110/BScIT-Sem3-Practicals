print("Insertion Sort")
A=[5,-1,2,7,3]
n=len(A)
print("A =",A)
for i in range(1,n):
    print("Pass -",i)
    temp=A[i]
    k=i-1
    while temp<A[k] and k>-1:
        A[k+1]=A[k]
        k=k-1
    A[k+1]=temp
    print("\tA:",A)