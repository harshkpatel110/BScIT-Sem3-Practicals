#empty queue
queue=[]
#enqueue
def INSERT(new_elt):
    queue.append(new_elt)
    print(new_elt,"is inserted into the queue.")
#dequeue
def DELETE():
    if queue:
        rem_elt=queue.pop(0)
        print(rem_elt,"is deleted from the queue.")
    else:
        print("The Queue is EMPTY.")
#display
def DISPLAY():
    print("Queue :",queue)
#Example Simulation
ch=1
while ch>0 and ch<4:
    print("Enter your choice :")
    ch=int(input("1.INSERT\n2.DELETE\n3.DISPLAY\n"))
    if ch==1:
        new_elt=input("Enter the element :")
        INSERT(new_elt)
    elif ch==2:
        DELETE()
    elif ch==3:
        DISPLAY()
    else:
        break