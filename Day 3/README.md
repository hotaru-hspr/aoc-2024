### Day 3

### Part 1

The input file is read, after which we search for occurences of the expected pattern "mul(<1-3 digit integer>,<1-3 digit integer>)", which can be done using regex. The expression for the pattern to look for is `mul\((\d{1,3}),(\d{1,3})\)`.

We get a list of tuples containing two strings of numbers of 1-3 digits each, that satisfy the regex given. We then calculate the sum of products of the numbers in the tuples present in the list.

One-liner for this part coz why not. Took more time to look up how to import a module within a statement than creating the solution itself.

### Part 2

#### Solution 1

At first glance, it is largely similar to the first part, but the "do()" and "don't()" flags present in the input need to be considered. Hence, we extend the original regex with expressions to identify the 'do' and 'don't' flags present (`mul\((\d{1,3}),(\d{1,3})\)`).

The input file is read and searched for matches for the above regex. We also initialise a variable to keep track of the "enabled" status, and a 'sum' variable to calculate the sum of products. As mentioned in the problem, the status is enabled at the beginning.

The matches are then iterated through and checked whether if it is a do/don't flag, in which case the enabled variable is switched to `True/False` based on whether "do()" or "don't()" is encountered.

If "mul(x,y)" is encountered, the 'enabled' status is checked, and if true, processed to calculate the product of numbers given, and added to the 'sum' variable.

On completion of iteration, the final sum is printed.

#### Solution 2

Initial code made for Part 2. Pretty stupid code, but it works, so...

The input file is read and searched for index values of occurences of the string "don't()" (regex `don't\(\)`). We do this to understand where the "don't()" strings exist and avoid them from being considered.

The list of valid tuples is initialised by processing the string with the regex until the first "don't()" is encountered.

We then iterate through the difference indices in the list of indices where "don't()" is present, and accessing the substring between the two indices. This substring is then split where "do()" is present (if any).

What this essentially does is split the disabled and enabled parts of the string into a list of substrings, with the disabled part always being at index 0 of the list. We skip this index and iterate through the other indices (enabled parts), search for substrings that match the regex, and extend the original list of valid tuples with the newly-found list of valid tuples.

Finally, we calculate the sum of products of the numbers in the tuples present in the list of valid tuples.

There are definitely more proper code than this (like the one above).
