#Creating an empty stack of size 5
n=5
stack=[None]*n
top=-1
#PUSH Operation
def push():
    global top
    if top==n-1:
        print("Stack Overflow")
    else:
        x=int(input("Enter the element : "))
        top+=1
        stack[top]=x
        print(x,"is pushed on the stack.")
#POP Operation
def pop():
    global top
    if top==-1:
        print("Stack Underflow")
    else:
        x=stack[top]
        print(x,"is popped from the stack.")
        stack[top]=None
        top-=1
#DISPLAY Operation
def display():
    if top==-1:
        print("Stack is empty.")
    else:
        print("Stack elements are : ")
        for i in range(top,-1,-1):
            print(stack[i])
#MAIN Program
ans=1
while ans!=4:
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("4. EXIT")
    ans=int(input("Enter your choice : "))
    if ans==1:
        push()
    elif ans==2:
        pop()
    elif ans==3:
        display()
    elif ans==4:
        print("Terminating the program...")
    else:
        print("Please enter a valid option.")