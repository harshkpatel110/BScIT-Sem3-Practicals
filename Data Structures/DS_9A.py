print("Inserting an element")
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
new_elt=int(input("\nEnter the new element :"))
k=int(input("Position No. :"))
i=n-1
while i>=k-1:
    a[i+1]=a[i]
    i=i-1
a[k-1]=new_elt
n=n+1
print("Array :",end=" ")
for i in range(n):
    print(a[i],end=" ")