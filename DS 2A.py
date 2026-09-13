A=[10,5,-1,0,7]
n=len(A)
data_mil_gaya=False
data=(int(input("Aapko kya search karna hai?")))
for i in range(1,n):
    if A[i]==data:
        print("The element is present in the array at the position",i)
        data_mil_gaya=True
if data_mil_gaya==False:
    print("The element is not present in the array.")
