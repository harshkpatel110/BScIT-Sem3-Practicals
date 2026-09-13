def pre_order(root):
    if t[root]=='-':
        return
    else:
        print(t[root],end=" ")
    left=(2*root)+1
    right=(2*root)+2
    if left<n:
        if t[left]!='-':
            pre_order(left)
    if right<n:
        if t[right]!='-':
            pre_order(right)
    return
def in_order(root):
    if t[root]=='-':
        return
    left=(2*root)+1
    right=(2*root)+2
    if left<n:
        if t[left]!='-':
            in_order(left)
    print(t[root],end=" ")
    if right<n:
        if t[right]!='-':
            in_order(right)
    return
def post_order(root):
    if t[root]=='-':
        return
    left=(2*root)+1
    right=(2*root)+2
    if left<n:
        if t[left]!='-':
            post_order(left)
    if right<n:
        if t[right]!='-':
            post_order(right)
    print(t[root],end=" ")
    return
# Main Program
print("Binary Tree")
h=int(input("Height of the tree : "))
n=(2**(h+1))-1
print("No. of nodes = ",n)
t=[]
print("Enter the array : ")
for i in range(n):
    print(i,".",end=" ")
    x=input()
    t.append(x)
print("Parent\tLeft\tRight")
#Parent=k, Left=2k+1, Right=2k+2
for i in range(n//2):
    print(i,".",end=" ")
    print(t[i],"\t",t[(2*i)+1],"\t",t[(2*i)+2])
    print()
print("\nPre Order Traversal : ",end=" ")
pre_order(0)
print("\nIn Order Traversal : ",end=" ")
in_order(0)
print("\nPost Order Traversal : ",end=" ")
post_order(0)