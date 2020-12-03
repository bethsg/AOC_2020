#In[0]
import numpy as np
expense_report = np.loadtxt("Input1.txt")

#In[1]
flag = False
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
    

#In[3]
arr0 = expense_report
arr1 = arr0
arr2 = arr1
flag = False

while(not flag):
    arrO = arr1
    arr1 = arr1[1:]
    arr2 = arr1[1:]
    for i in arr1:
        for j in arr2:
            if arr0[0] + i + j == 2020:
                print(arr0[0]*i*j)
                flag = True
            if flag:
                break
        if flag:
            break
# %%
