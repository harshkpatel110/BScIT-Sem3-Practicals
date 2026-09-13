print("\nLinear Search")
A=[73,18,10,5,21,32,74]
print("A =",A)
data=int(input("Enter the element to be searched :"))
n=len(A)
flag=0
for i in range(n):
    if A[i]==data:
        flag=1
        break
if flag==0:
    print("The element is not present in the Array.")
else:
    print("The element is present in the Array at position ",i)