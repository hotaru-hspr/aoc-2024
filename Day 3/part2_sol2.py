import re
regex = "mul\((\d{1,3}),(\d{1,3})\)"

data = open("input.txt").read()
ind = [i.start() for i in re.finditer("don't\(\)",data)]
val = re.findall(regex, data[:ind[0]])

for i in range(len(ind)-1):
    nums = data[ind[i]:ind[i+1]].split("do()")
    for j in nums[1:]:
        val.extend(re.findall(regex, j))
    
print(sum(int(c)*int(d) for c,d in val))