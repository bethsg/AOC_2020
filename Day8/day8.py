#In[]
import numpy as np
boot_code = np.loadtxt("Input8.txt", dtype=str)
accumulator = 0
pointer = 0
print(boot_code)
#In[]
def acc(operand):
    return (accumulator+operand, pointer+1)
def jmp(operand):
    return pointer + operand
def nop():
    return pointer + 1

#In[]
visited = np.zeros(len(boot_code))
while True:
    if visited[pointer] == 0:
        visited[pointer] = 1
        if boot_code[pointer][0] == "acc":
            accumulator, pointer = acc(int(boot_code[pointer][1]))
        elif boot_code[pointer][0] == "jmp":
            pointer = jmp(int(boot_code[pointer][1]))
        else:
            pointer = nop()
    else:
        print(accumulator)
        break

#In[]

def terminates(code):
    p = 0
    a = 0
    v = np.zeros(len(code))
    while True:
        if p == len(code):
            return (True, a)
        if v[p] == 0:
            v[p] = 1
            if code[p][0] == "acc":
                a = a + int(code[p][1])
                p = p + 1
            elif code[p][0] == "jmp":
                p =  p + int(code[p][1])
            elif code[p][0] == "nop":
                p = p + 1
        else:
            return (False, a)

for i in range(0, len(boot_code)):
    boot_dupe = np.loadtxt("Input8.txt", str)
    if boot_code[i][0] == "jmp":
        boot_dupe[i][0] = "nop"
    elif boot_code[i][0] == "nop":
        boot_dupe[i][0] = "jmp"
    finishes, total = terminates(boot_dupe)
    if finishes:
        print(total)
        


# %%
