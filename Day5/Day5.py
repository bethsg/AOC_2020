#In[]
import numpy as np
passes = np.loadtxt("Input5.txt", str)
#In[]
seats = []
highest_seat_id = 0
for bpass in passes:
    rows = np.arange(128)
    column = np.arange(8)
    for char in bpass:
        if char == 'F':
            rows = rows[:int(len(rows)/2)]
        elif char == 'B':
            rows = rows[int(len(rows)/2):]
        elif char == 'R':
            column = column[int(len(column)/2):]
        elif char == 'L':
            column = column[:int(len(column)/2)]
    seats.append(rows[0]*8 + column[0])

print(max(seats))

#In[]
seats = sorted(seats)

for x in range(0, len(seats)-1):
    if seats[x+1] - seats[x] == 2:
        print(seats[x]+1)

# %%
