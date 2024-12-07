word_pos = {('M','A','S'), ('S','A','M')}
grid = [line.strip() for line in open("input.txt").readlines()]
c = 0

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if grid[i][j] == 'A':
            x = (grid[i-1][j-1], grid[i][j], grid[i+1][j+1])
            y = (grid[i-1][j+1], grid[i][j], grid[i+1][j-1])
            if x in word_pos and y in word_pos:
                c += 1
print(c)