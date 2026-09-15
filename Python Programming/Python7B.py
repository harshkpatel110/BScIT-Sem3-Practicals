d={'b':2,'a':1,'d':4,'c':3}
print("Ascending order:")
for key in sorted(d):
    print(key,":",d[key])
print("Descending order:")
for key in sorted(d,reverse=True):
    print(key,":",d[key])