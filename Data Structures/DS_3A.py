print("Hashing Techniques : Division Remainder Method")
m=int(input("Size of the hash table : "))
n=int(input("Number of Keys : "))
h=[]
for i in range(m):
    h.append(0)
print("Enter elements")
for i in range(n):
    key=int(input())
    rel_add=key%m
    if h[rel_add]==0:
        h[rel_add]=key
        print("Relative Address =",rel_add)
    else:
        print("Relative Address =",rel_add,"(Collision Case)")
print("\nHash Table")
print("Index\tKey")
for i in range(m):
    print(i,"\t",h[i])