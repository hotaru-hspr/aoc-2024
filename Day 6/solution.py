grid = [list(line.strip()) for line in open("input.txt").readlines()]

for line in range(len(grid)):
    for char in range(len(grid[0])):
        if grid[line][char] == '^':
            x, y = line, char
            break


directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
curdir = 0
ox, oy = x, y
positions = {(x,y)}
gl, gh = len(grid), len(grid[0])

while True:
    nx = x + directions[curdir % 4][0]
    ny = y + directions[curdir % 4][1]
    
    if not (0 <= nx < gl and 0 <= ny < gh):
        break
    if grid[nx][ny] != '#':
        x, y = nx, ny
        positions.add((x,y))
    else:
        curdir = (curdir + 1) % 4

c2 = 0
for (i,j) in positions:
    visited = set()
    if grid[i][j] == '.':
        grid[i][j] = '#'
        x, y, curdir = ox, oy, 0
        while True:
            nx = x + directions[curdir % 4][0]
            ny = y + directions[curdir % 4][1]
            
            if not (0 <= nx < gl and 0 <= ny < gh):
                break
            if (nx,ny,curdir) in visited:
                c2 += 1
                break
            if grid[nx][ny] != '#':
                x, y = nx, ny
                visited.add((x,y,curdir))
            else:
                curdir = (curdir + 1) % 4
        grid[i][j] = '.'

print(f"Part 1: {len(positions)}")
print(f"Part 2: {c2}")