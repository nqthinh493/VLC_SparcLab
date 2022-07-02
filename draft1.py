from matplotlib.pyplot import flag
import numpy as np

from simulator import Sensor_status
a = [0,0,0,0,0,1,1,1,1,2,2,2,3,3,3]
print(len(a))
arr = np.array(a)
flags = [0]
for i,x in enumerate(arr):
    if i+1 != len(a):
        if arr[i] != arr[i+1]:
            flags.append(i+1)
flags.append(len(arr)+1)
print(flags)
for i in range(len(flags)):
    if  i+1!= len(flags):
        brr= arr[flags[i]:flags[i+1]]   
        print(brr)
        
def Split_frame(Symbols_status):
    print(len(Symbols_status))
    Sensor_status = []
    flags = [0]
    for i,x in enumerate(Symbols_status):
        if i+1 != len(Symbols_status):
            if Symbols_status[i][2] != Symbols_status[i+1][2]:
                flags.append(i+1)
    flags.append(len(Symbols_status)+1)
    print(flags)
    for i in range(len(flags)):
        if  i+1!= len(flags):
            brr= arr[flags[i]:flags[i+1]]   
            Sensor_status.append(brr)
    return flags