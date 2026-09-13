#PUSH Operation
def push(elt):
    global s
    global top
    if top==n-1:
        print("Stack Overflow")
    else:
        top+=1
        s[top]=elt
#POP Operation
def pop():
    global s
    global top
    if top==-1:
        print("Stack Underflow")
    else:
        data=s[top]
        s[top]=None
        top-=1
    return data
#DISPLAY Stack
def display_stack():
    if top==-1:
        print("Stack : NULL")
    else:
        print("Stack : ",end=" ")
        for i in range(top+1):
            print(s[i],end=" ")
#DISPLAY Postfix Expression
def display_postfix () :
    print ("\nPostfix Expression : ", end=" ")
    print (postfix)
#To find the priority of element
def priority(elt) :
    if elt=="+" or elt=="-":
        return 1
    elif elt=="*" or elt=="/":
        return 2
    elif elt=="^":
        return 3
    else:
        return 0
#MAIN Program
exp=input("Enter the infix Expression : ")
exp="("+exp+")"
n=len(exp)
s=[None]*n
top=-1
postfix=""
for i in range(n):
    a=exp[i]
    print("\nCharacter scanned : ",a)
    if a=="(":
        push(a)
    elif a=="+" or a=="-" or a=="*" or a=="/" or a=="^":
        p_a=priority(a)
        p_top_elt=priority(s[top])
        if p_a<=p_top_elt:
            while p_a<=p_top_elt:
                y=pop()
                postfix=postfix+y
                p_top_elt=priority(s[top])
        push(a)
    elif a==")":
        b=s[top]
        while b!="(":
            y=pop()
            postfix=postfix+y
            b=s[top]
        pop() # to pop "("
    else:
        postfix=postfix+a
    display_stack()
    display_postfix()