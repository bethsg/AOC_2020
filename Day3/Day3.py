#In[]
import pandas as pd
tree_map = pd.read_table("Input3.txt",header=None)
print(32%31)
#In[]
count = 0
x = 0
for y in range(0, 323):
    if tree_map[0][y][x] == '#':
        count = count + 1
    x = (x + 3)%31
print(count)

#In[]
def tree_detection(down,right):
    counter = 0
    x = 0
    for y in range(0,323,down):
        if tree_map[0][y][x] == '#':
            counter = counter + 1
        x = (x + right)%31
    return counter

tree_detection(1,3)*tree_detection(1,1)*tree_detection(1,5)*tree_detection(1,7)*tree_detection(2,1)
# %%
