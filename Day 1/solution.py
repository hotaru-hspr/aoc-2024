x , y = [], []
for i in open("input.txt").readlines():
  x.append(int(i.split()[0]))
  y.append(int(i.split()[1]))
x.sort()
y.sort()
print(f"Task 1: {sum([abs(x[i]-y[i]) for i in range(len(x))])}")
print(f"Task 2: {sum([x[i]*y.count(x[i]) for i in range(len(x))])}")
