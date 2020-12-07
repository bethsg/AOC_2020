#In[]
with open("Input6.txt") as f:
    inputt  = f.read()
groups  = inputt.split("\n\n")
groups[-1] = groups[-1][:-1]

alphabet = set("abcdefghijklmnopqrstuvwxyz")
#In[]
sum_of_answers = 0
for group in groups:
    group_answers = 0
    for char in alphabet:
        if char in group:
            group_answers = group_answers + 1
    sum_of_answers = sum_of_answers + group_answers

print(sum_of_answers)
    
#In[]
sum_of_counts = 0
for group in groups:
    group_size = len(group.split('\n'))
    for char in alphabet:
        if group_size == group.count(char):
            sum_of_counts = sum_of_counts + 1
print(sum_of_counts)


# %%
