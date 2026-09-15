file=open("sample.txt","r")
lines=file.readlines()
n=int(input("Enter the number of lines:"))
for line in lines[-n:]:
    print(line,end=" ")
file.close()