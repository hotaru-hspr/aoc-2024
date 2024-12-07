def safeAndSorted(lst):
  return all(1 <= abs(lst[i+1]-lst[i]) <= 3 for i in range(len(lst)-1)) and (all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or all(lst[i] >= lst[i+1] for i in range(len(lst)-1)))

c1, c2 = 0, 0
for line in open("input.txt").readlines():
    nums = list(map(int, line.split()))
    if safeAndSorted(nums):
        c1 += 1
    else:
        for i in range(len(nums)):
            if safeAndSorted(nums[:i] + nums[i+1:]):
                c2 += 1
                break
            
print(f"Part 1: {c1}")
print(f"Part 2: {c1+c2}")