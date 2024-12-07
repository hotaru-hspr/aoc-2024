### Day 2

### Part 1

The file is read, each line iterated through, and made into a list of numbers. A function `safeAndSorted(list)` is defined early on in the program, which checks the two conditions required in this problem: whether it's sorted in ascending/descending order, and if the sequence is safe (i.e. difference between two consecutive values should be at least 1 and at most 3).

The lists of numbers are passed through the function, and if deemed safe by the function, increments the counter variable by 1, which is printed at the end of the program.

### Part 2

The function is defined and the file is read, similar to Part 1.

The lists of numbers are passed through the function, and if deemed safe and sorted by the function, increments the counter variable by 1. If not, this is where Part 2's condition of having a "Problem Dampener" comes in, where we can avoid one number in the list to satisfy the function's conditions.

We iterate through the list to generate sublists without one number in each iteration, and pass it to the `safeAndSorted(sublist)` function. When a sublist satisfies the function's conditions, the counter is incremented by 1 and any further generation of sublists is stopped.

### Personal Notes

Made this solution while travelling back home on a train, with the Replit app on my phone. Felt too awkward to open my laptop amongst a group of elderly people, as if coding on a phone wasn't awkward enough.
