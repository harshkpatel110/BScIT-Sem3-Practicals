print("Hashing Ttechniques with Seaparate Chaining as a Collision Resolution Technique(Table Size 5)")
h0=[]
h1=[]
h2=[]
h3=[]
h4=[]

n=int(input("Number of Keys: "))
print("Enter Elements: ")
for i in range(n):
    key=int(input())
    rel_add=key%5
    if rel_add==0:
        h0.append(key)
    elif rel_add==1:
        h1.append(key)
    elif rel_add==2:
        h2.append(key)
    elif rel_add==3:
        h3.append(key)
    elif rel_add==4:
        h4.append(key)
print("\nHash Table")
print(h0)
print(h1)
print(h2)
print(h3)
print(h4)
