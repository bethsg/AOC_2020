#In[]
import numpy as np
encrypted_data = np.loadtxt("Input9.txt",int)
# %%
pointer = 25
is_valid = True
while is_valid:
    is_valid = False
    for x in encrypted_data[pointer-25:pointer]:
        for y in encrypted_data[pointer-25:pointer]:
            #print(x, y)
            if x != y and x + y == encrypted_data[pointer]:
                is_valid = True
    if is_valid:
        pointer = pointer + 1
invalid_number = encrypted_data[pointer]
print(invalid_number)
#In[]
for x in range(0, len(encrypted_data)-1):
    for y in range(x+1, len(encrypted_data)):
        if sum(encrypted_data[x:y+1]) == invalid_number:
            print(max(encrypted_data[x:y+1]) + min(encrypted_data[x:y+1]))
# %%
