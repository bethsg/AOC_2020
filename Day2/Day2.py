#In[]
import numpy as np
passwords = np.loadtxt("Input2.txt", str)

#In[]
count = 0
for n in range(0, len(passwords)):
    temp = passwords[n,2].count(passwords[n,1][0])
    low, high = passwords[n,0].split("-")
    low = int(low)
    high = int(high)
    if low <= temp <= high:
        count = count + 1
print(count)
# %%
# %%
