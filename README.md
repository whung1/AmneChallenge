# AmneChallenge
Challenge at https://www.amne.co/challenge/

## Problem Description

As Amne expands, we will want to understand large-scale patterns in home values.

As we look at patterns across windows of certain sizes, we will need to efficiently track trends such as increasing and decreasing subranges.

For this problem, you are given N days of average home sale price data, and a fixed window size K . For each window of K days, from left to right, find the number of increasing subranges within the window minus the number of decreasing subranges within the window.

A window of days is defined as a contiguous range of days. Thus, there are exactly N-K+1 windows where this metric needs to be computed. An increasing subrange is defined as a contiguous range of indices [a,b], a < b , where each element is larger than the previous element. A decreasing subrange is similarly defined, except each element is smaller than the next.

### Constraints

1 ≤ N ≤ 200,000 days
1 ≤ K ≤ N days
Input Format

Your solution should accept an input file (input.txt) with the following contents: 

 Line 1: Two integers, N and K.
 Line 2: N positive integers of average home sale price, each less than 1,000,000.

### Output Format

Your solution should output one integer for each window’s result, with each integer on a separate line, to an output file or to the console.

### Sample Input
```
5 3
188930 194123 201345 154243 154243
```
### Sample Output
```
3
0
-1
```
### Explanation

For the first window of [188930, 194123, 201345], there are 3 increasing subranges ([188930, 194123, 201345], [188930, 194123], and [194123, 201345]) and 0 decreasing, so the answer is 3. For the second window of [194123, 201345, 154243], there is 1 increasing subrange and 1 decreasing, so the answer is 0. For the third window of [201345, 154243, 154243], there is 1 decreasing subrange and 0 increasing, so the answer is -1.

### Performance

Your solution should run in less than 30 seconds and use less than 50MB of memory with a valid input of any size (within the given constraints).

## Problem Solution Logic

For a list of numbers of size n, we need to check windows of k size within the list.
Since the each previous window gives no particularly useful insights on the next window given that continuously increaasing or decreasing subranges will change dynamically based on order.
Thus, we should try to simplify the calculation of the total summation of a continuously increasing or decreasing subrange of size m where 2<=m<=k
We notice that for each m, m+1 = (m-1)+sum(m-1) where sum(m) is the sum of all continuous subranges of size m

Example:
    Lets say we have a sub-window of [1, 2, 3, 4, 5] where it is continuously increasing.
    base case: [1] = m=1, has 0 subranges, sum(1) = 0
    [1, 2] = first subrange, base case m=2, sum(m) = 1 + 0 = m-1 + sum(m-1) = 0
    [1, 2, 3] = m=3, notice that adding 3 means it increases by the number of interactions with each former element of the subrange
    in this case, [1, x, 3], [2, 3] since the values in middle are irrelevant as long as it is continuous with the trend.
    Thus after including the previous subrange [1,2], sum(m+1) = 2 + 1 = (m-1) + sum(m-1) = 3
    [1, 2, 3, 4] = m=4, like the previous case, we get the new additions [1, x, x, 4] [2, x, 4] [3, 4] to the previous ones
    Thus, sum(m) = 3 + 3 = 6 = (m-1) + sum(m-1)

    
