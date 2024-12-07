x , y = [], []

for i in open("input.txt").readlines():
  x.append(int(i.split()[0]))
  y.append(int(i.split()[1]))
x.sort()
y.sort()

print(f"Task 1: {sum([abs(a-b) for a,b in zip(x,y)])}")
print(f"Task 2: {sum([i*y.count(i) for i in x])}")