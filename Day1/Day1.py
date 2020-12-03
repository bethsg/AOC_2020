#In[0]
import numpy as np
expense_report = np.loadtxt("Input1.txt")

#In[1]
flag = False
i = 0
curr_arr = expense_report
comp_arr = curr_arr

#In[2]
while(not flag):
    curr_arr = comp_arr
    comp_arr = comp_arr[1:]
    for n in comp_arr:
        if n + curr_arr[0] == 2020:
            flag = True
            print(n*curr_arr[0])
            break
    

# %%
