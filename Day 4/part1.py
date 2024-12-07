word = "XMAS"
grid = [line.strip() for line in open("input.txt").readlines()]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
wl = len(word)
c = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        for x, y in directions:
            if 0 <= i + (wl - 1) * x < len(grid) and 0 <= j + (wl - 1) * y < len(grid[0]):
                match = True
                for k in range(wl):
                    a = i + k * x
                    b = j + k * y
                    if grid[a][b] != word[k]:
                        match = False
                        break
                if match:
                    c += 1
print(c)
