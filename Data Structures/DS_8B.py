#empty queue
queue=[]
#enqueue
def arrive(c_name):
    queue.append(c_name)
    print(c_name,"has arrived.")
#dequeue
def serve():
    if queue:
        served=queue.pop(0)
        print(served,"is being served.")
    else:
        print("No customers in the queue.")
#display
def show_queue():
    print("Waiting Queue :",queue)
#Example Simulation
ch=1
while ch>0 and ch<4:
    print("Enter your choice :")
    ch=int(input("1.New Customer\n2.Customer presently being served\n3.Waiting Customer\n"))
    if ch==1:
        c_name=input("Enter customer name :")
        arrive(c_name)
    elif ch==2:
        serve()
    elif ch==3:
        show_queue()
    else:
        break