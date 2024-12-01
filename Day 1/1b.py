x , y, s = [], [], 0
for i in open("input.txt").readlines():
  x.append(int(i.split()[0]))
  y.append(int(i.split()[1]))
x.sort()
y.sort()
s = sum([x[i]*y.count(x[i]) for i in range(len(x))])
print(s)