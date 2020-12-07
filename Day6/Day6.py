#In[]
with open("Input6.txt") as f:
    inputt  = f.read()
groups  = inputt.split("\n\n")

alphabet = set("abcdefghijklmnopgrstuvwxyz")

sum_of_answers = 0
for group in groups:
    group_answers = 0
    for char in alphabet:
        if char in group:
            group_answers = group_answers + 1
    sum_of_answers = sum_of_answers + group_answers

print(sum_of_answers)
    
# %%
