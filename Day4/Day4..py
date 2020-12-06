#In[]
import re
with open("Input4.txt") as f:
    inputt  = f.read()
inputt  = inputt.split("\n\n")
passports = []
for passport in inputt:
    fields = {}
    for field in re.split('\n| ',passport):
        if len(field.split(':')) == 2:
            key, value = field.split(':')
            fields[key] = value
    passports.append(fields)

#In[]
counter = 0
for element in passports:
    if 'byr' in element and 'iyr' in element and 'eyr' in element and 'hgt' in element and 'ecl' in element and 'pid' in element and 'hcl' in element:
        counter = counter + 1
print(counter)
# %%
