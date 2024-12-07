import re
regex = "mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"

def mul(a,b):
    return int(a)*int(b)

sum = 0
iterList = re.finditer(regex,open("input.txt").read())
enabled = True

for itr in iterList:
    itr = itr.group()
    if itr == "do()":
        enabled = True
    elif itr == "don't()":
        enabled = False
    elif enabled == True:
        sum += eval(itr)
    
print(sum)