print("Deleting an element")
arr_size=int(input("Enter the size of the array :"))
a=[]
for i in range(arr_size):
    a.append(0)
n=int(input("No. of elements :"))
print("Enter all elements :")
for i in range(n):
    a[i]=int(input())
print("Array :",end=" ")
for i in range(n):
    print(a[i],end=" ")
k=int(input("\nPosition No. :"))
i=k-1
while i<n-1:
    a[i]=a[i+1]
    i=i+1
n=n-1
print("Array :",end=" ")
for i in range(n):
    print(a[i],end=" ")