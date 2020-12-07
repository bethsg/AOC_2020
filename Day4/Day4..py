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
valid_fields = []
for element in passports:
    if 'byr' in element and 'iyr' in element and 'eyr' in element and 'hgt' in element and 'ecl' in element and 'pid' in element and 'hcl' in element:
        counter = counter + 1
        valid_fields.append(element)
print(counter)
# In[]
def is_hex(s):
    hex_digits = set("0123456789abcdef")
    if s[0] == '#' and len(s) == 7:
        for char in s[1:]:
            if not (char in hex_digits):
                return False
        return True
    else:
        return False
counter = 0
for entry in valid_fields:
    flag = True
    if not(1920 <= int(entry['byr']) <= 2002 and len(entry['byr']) == 4):
        flag = False
    if not(2010 <= int(entry['iyr']) <= 2020 and len(entry['iyr']) == 4):
        flag = False
    if not(2020 <= int(entry['eyr']) <= 2030 and len(entry['eyr']) == 4):
        flag = False
    if entry['hgt'][-2:] == 'cm':
        if not(150 <= int(entry['hgt'][:-2]) <= 193):
            flag = False
    elif entry['hgt'][-2:] == 'in':
        if not(59 <= int(entry['hgt'][:-2]) <= 76):
            flag = False
    else:
        flag = False
    if not(is_hex(entry['hcl'])):
        flag = False
        print(entry['hcl'])
    if entry['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
        flag = False
    
    if not(len(entry['pid']) == 9) or not(entry['pid'].isdigit()):
        flag = False
    if flag:
        counter = counter + 1
print(counter)
# %%
