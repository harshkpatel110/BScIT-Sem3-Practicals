import numpy as np
arr=np.array([10,20,30])
b=arr
copy_arr=arr.copy()
arr[0]=100
print("Original Array:\t",arr)
print("Alias Array:\t",b)
print("Copied Array:\t",copy_arr)