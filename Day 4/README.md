### Day 4

### Part 1

In this problem, we need to find occurences of "XMAS" in a 2D grid in all 8 possible directions (horizontal, vertical & diagonal).

Here, we read the lines of the input file, and initiate a list of tuples containing values for different directions, representing the unit change in the X and Y axes in the respective direction.

We traverse through the rows and columns of the grid, and for each position, we iterate through the different possible directions. For each direction, we check if the boundary conditions are satisfied before checking for a match with "XMAS".

Each iteration of "XMAS" is compared with the position in the grid in the current direction, and if the entire word is a match, the counter variable is incremented by 1.

The final count of occurences of "XMAS" in the grid is printed at the end.

### Part 2

Here, we need to find the count of occurences where two "MAS" strings in any diagonal direction form a X-shape, i.e.:

```
M S
 A
M S
```

(Note: The "MAS" can be in any diagonal direction.)

We traverse through the rows and columns of the grid in search of the common character 'A', avoiding the top and bottom rows, and the left and right columns, as they are boundary conditions and don't have further columns for comparison.

When we encounter an 'A' in the grid, we check if the elements in both diagonals centered around it form "MAS", and if yes, increment the counter variable by one.

The final count of occurences of "X-MAS" (two overlapping MAS strings) in the grid is printed at the end.
