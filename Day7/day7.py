#In[]
import numpy as np
data = np.loadtxt("Input7.txt", str, delimiter="\n")
bagdict = {}
for datapoint in data:
    deets = datapoint.split(" ")
    key = deets[0] + " " + deets[1]
    value = []
    if deets[4] != "no":
        for x in range(0,int((len(deets)-4)/4)):
            bag = deets[5 + 4*x] + " " + deets[6 + 4*x]
            bagno = (bag,deets[4 + 4*x])
            value.append(bagno)
    bagdict[key] = value     

print(("faded violet" in bagdict["shiny beige"][0]))
#In[]
def search(key):
    if not bagdict[key]:
        return False
    elif any("shiny gold" in x for x in bagdict[key]):
        return True
    else:
        flag = False
        for bag in bagdict[key]:
            flag = flag or search(bag[0])
        return flag
bags_containing_gold = 0
for colour, _ in bagdict.items():
    if search(colour):
        bags_containing_gold = bags_containing_gold + 1
print(bags_containing_gold)

#In[]
def bags_in(key):
    if not bagdict[key]:
        return 1
    else:
        total = 0
        for bag in bagdict[key]:
            total = total + int(bag[1])*bags_in(bag[0])
        return total + 1
print(bags_in("shiny gold"))

# %%
a, b = (1,2)
print(a)

# %%
