A=[-1,0,5,7,10]
n=len(A)
start=0
end=n-1
data_mil_gaya=False
print("A=",A)
data=(int(input("Aapko kya search karna hai?")))
while start<=end:
    mid=int((start+end)/2)
    print("s=",start)
    print("e=",end)
    print("mid=",mid)
    if data==A[mid]:
        print("The element is present in the array at the position",mid)
        data_mil_gaya=True
        exit
    if data>A[mid]:
        start=mid+1
    else:
        end=mid-1
if data_mil_gaya==False:
    print("The element is not present in the array.")
