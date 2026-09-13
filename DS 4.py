print("Binary Search Tree")
n=int(input("No. of Elements : "))
h=n-1
t=[]
arr_size=(2**(h+1))-1
for i in range(arr_size):
    t.append(0)
print("Enter the element : ")
for i in range(n):
    print(i+1,end=" ")
    x=int(input())
    if i==0:
        t[i]=x
    else:
        root=0
        while t[root]!= 0:
            if x<t[root]:
                root=(2*root)+1
            elif x>=t[root]:
                root=(2*root)+2
        t[root]=x
print("Parent\tLeft\tRight")
for i in range(arr_size//2):
    if t[i]>0:
        print(t[i],"\t",t[(2*i)+1],"\t",t[(2*i)+2])
for k in range(3):
    elt=int(input("Enter the element to be searched : "))
    root=0
    flag=0
    for i in range(n):
        if elt==t[root]:
            print(elt,"=",t[root])
            flag=1
            break
        elif elt<t[root]:
            print(elt,"<",t[root],"Move to L.H.S.")
            root=(2*root)+1
        else:
            print(elt,">",t[root],"Move to R.H.S.")
            root=(2*root)+2
        if t[root]==0:
            break
    if flag==0:
        print("The element is not present in the BST.")
    else:
        print("The element is present in the BST.")