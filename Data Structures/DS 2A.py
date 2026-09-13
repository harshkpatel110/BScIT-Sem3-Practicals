print("Linear Search")
A=[73,18,10,5,21,32,74]
print("A =",A)
n=len(A)
data=int(input("Enter the element to be searched : "))
for i in range(n):
    if data==A[i]:
        print(f"The element {data} is present in the array at position {i}.")
        break
else:
    print(f"The element {data} is not present in the array.")