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
# In[]
count = 0
for n in range(0, len(passwords)):
    pos1, pos2 = passwords[n,0].split("-")
    pos1 = int(pos1)
    pos2 = int(pos2)
    if (passwords[n,1][0] == passwords[n,2][pos1-1]) ^ (passwords[n,1][0] == passwords[n,2][pos2-1]):
        count = count + 1
print(count)
# %%
