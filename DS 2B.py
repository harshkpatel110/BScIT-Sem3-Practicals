print("Binary Search")
A=[10,20,25,51,75,100,250,500]
print("A=",A)
data=int(input("Enter the element to be searched: "))
n=len(A)
start=0
end=n-1
print("Start\tEnd\tMid")
while start<=end:
    mid=(start+end)//2
    print(f"{start}\t{end}\t{mid}")
    if data==A[mid]:
        print(f"The element {data} is present in the array at position {mid} in the array.")
        break
    elif data<A[mid]:
        end=mid-1
    else:
        start=mid+1
else:
    print(f"The element {data} is not present in the array.")