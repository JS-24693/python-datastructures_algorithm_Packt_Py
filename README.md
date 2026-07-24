# Foundations of Data Structures & Algorithms in Python Course - Packt

## 01_ArrayPractice.py

### Python Dynamic Arrays, List Operations, Comprehensions, and Slicing

#### Dynamic Arrays (Python Lists)

Python lists are dynamic arrays.
They store elements in a contiguous block of memory and resize automatically when capacity is exceeded.

#### Append Complexity

append() is amortized O(1)

Occasional resize steps cost O(n) due to copying all elements

A two‑element list begins with extra internal capacity, but the exact value is CPython‑dependent (not necessarily 4)

#### Dynamic Arrays Practice

- Create and Access Lists
- Append and Pop
- Iteration
- Sorting (O(n log n))
- Sorting with a key

#### List Comprehension Basics

- explicit loop equivalent
- create a list
- apply operations
- repeated values
- tuple generation (1D)
- conditional tuples

#### 2D lists 

- basic construction
- conditional construction

#### Slicing (O(k))

All slicing operations run in O(k) where k = number of returned elements.

Practice:
- base list
- explicit loop equivalent
- basic slices
- step slices
- reverse slice

## 02_MaxConsecOnes.py 

Leetcode 485 is listed in the course as a special case of maximum sum since the list values are binary, meaning lists of 0 and 1. 

For the first list of integer values, it outputs 3 because the algorithm counts consecutive 1s and resets on 0:
- Read 1 → count = 1
- Read 1 → count = 2
- Read 0 → count = 0
- Read 1 → count = 1
- Read 1 → count = 2
- Read 1 → count = 3

The longest streak is 3, so the method returns 3.

## 03_MaximumSum.py

Kadane’s algorithm is used to compute the **maximum subarray sum** in a list of integer values.  
Two running values are maintained:

- **current** — best sum ending at the current index  
- **best** — global maximum sum seen so far  

As the algorithm scans the list, it updates these values to track the highest‑value contiguous subarray.

#### Example: `[1, -2, 3, 5, -1, 2]`

The code outputs **9** because Kadane’s algorithm updates the running sum and global maximum at each step:

- Start: `current = 0`, `best = -inf`
- Read `1` → `current = 1`, `best = 1`
- Read `-2` → `current = -1`, `best = 1`
- Read `3` → `current = 3`, `best = 3`
- Read `5` → `current = 8`, `best = 8`
- Read `-1` → `current = 7`, `best = 8`
- Read `2` → `current = 9`, `best = 9`

**Final maximum subarray sum = 9.**

## 04_BuyAndSellAStock.py

LeetCode 121 defines the algorithm for determining the **best time to buy and sell a stock** when you are allowed **only one transaction** (one buy + one sell). The input is a list of integer values representing the **stock price on each day**, in order.

The test instantiations cover:
- a normal rising‑then‑falling sequence (profit **5**)
- a strictly decreasing sequence (profit **0**)
- a small list with one profitable sell (profit **2**)

#### Example 1: `[7,1,5,3,6,4]`

Each integer represents the stock price for that day:
- Day 1 price = 7  minValue = 7
- Day 2 price = 1  (1-7 = -6 profit)
- Day 3 price = 5  minValue = 1, (5-1 = 4 profit)
- Day 4 price = 3  (3-1 = 2 profit)
- Day 5 price = 6  (6-1 = 5 profit)
- Day 6 price = 4  (4-1 = 3 profit)

These values allow choosing **one day to buy** and **one later day to sell**.

**Best choice:**  
- Buy at **1** (day 2)  
- Sell at **6** (day 5)  
- Profit = **6 − 1 = 5**

## 05_ProductOfArrayExceptSelf.py

LeetCode 238 defines the algorithm for computing the **product of array elements except self** without using division.  
The goal is to return a new list where each position contains the product of **all other values** in the input list.

The algorithm uses two passes:

- **Left products** — running product of all values before each index  
- **Right products** — running product of all values after each index  

Each final value is the product of its corresponding left and right values.

#### Example 1: `[1,2,3,4]` 

The algorithm processes each index i and treats nums[i] as the "self" value for the iteration so it computes the product of all other values using the left and right product arrays. 

- When i = 0, self = 1  
Output uses: product of all values after 1 → 2×3×4
- When i = 1, self = 2  
Output uses: product of values before (1) × product after (3×4)
- When i = 2, self = 3  
Output uses: 1×2 × 4
- When i = 3, self = 4  
Output uses: 1×2×3

## 06_RotateArray.py

LeetCode 189 is a problem where you must rotate an array to the **right** by `k` steps.  
A right‑rotation means repeatedly taking the **last element** and moving it to the **front**.

Because performing each rotation individually is too slow (`O(n·k)`), the optimal solution uses the **three‑reversal method**:

1. Reverse the entire array  
2. Reverse the first `k` elements  
3. Reverse the remaining `n − k` elements  

Before doing this, `k` is reduced using `k % n` because rotating an array `n` times returns it to its original form.

#### Example 1: `[1,2,3,4,5,6,7]`, `k = 3`

Manual rotation (one step at a time):

- After 1 rotation → `7 1 2 3 4 5 6`  
- After 2 rotations → `6 7 1 2 3 4 5`  
- After 3 rotations → `5 6 7 1 2 3 4`

This matches the output produced by the reversal method.

#### Key Details

- Right‑rotation moves the last element to the front.  
- `k % n` ensures rotation count stays within array length.  
- The three‑reversal technique performs rotation in **O(n)** time.  
- This approach avoids the brute‑force `O(n·k)` simulation.

## 07_MaximumSumSubarray.py

This file implements Kadane’s Algorithm, the same method described in **03_MaximumSum.py**, to compute the **maximum subarray sum** for a list of integers. The algorithm maintains two running values:

- **current** — best sum ending at the current index  
- **best** — global maximum sum seen so far  

At each step, the running sum is either extended or restarted depending on whether adding the next value improves the total.

### Example: `[1, -2, 3, 5, -1, 2]`

Kadane’s Algorithm updates the running sum and global maximum as it scans the list:

- Start: `current = 0`, `best = -inf`  
- Read `1` → `current = 1`, `best = 1`  
- Read `-2` → `current = -1`, `best = 1`  
- Read `3` → `current = 3`, `best = 3`  
- Read `5` → `current = 8`, `best = 8`  
- Read `-1` → `current = 7`, `best = 8`  
- Read `2` → `current = 9`, `best = 9`  

**Final maximum subarray sum = 9.**

This implementation follows the same logic: track a running sum, reset when negative, and update the global maximum.

## 08_MaximumProductSubarray.py

LeetCode 152 is a problem where you must compute the **maximum product of any contiguous subarray**.  
Unlike the maximum‑sum problem, the product version is more complex because:

- negative numbers can flip the sign  
- zeros break the array into independent segments  
- the maximum product may come from multiplying two negative values  

To handle these cases correctly, the algorithm maintains two running values at each index:

- **maxP** — maximum product ending at the current index  
- **minP** — minimum product ending at the current index  

Tracking both is essential because a negative number can turn the minimum product into a new maximum.

#### Example: `[0, 2, -5, -2, 4, 0, 3, -1]`

Zeros split the array into segments:

##### Segment 1: `[2, -5, -2, 4]`

Products:
- `2 * -5 = -10`
- `-10 * -2 = 20`
- `20 * 4 = 80` ← maximum in this segment

##### Segment 2: `[3, -1]`

Products:
- `3 = 3`
- `3 * -1 = -3`

Maximum in this segment is `3`.

##### Final maximum product

`max(80, 3) = 80`

This matches the algorithm’s output.

#### Key Details

- Negative values require tracking both max and min products.  
- Zeros reset the running product.  
- The algorithm runs in **O(n)** time using a single pass.  
- The maximum product subarray may span multiple negative values.

## 09_ValidSudoku.py

This file implements validation logic for a 9×9 Sudoku board.  

A board is valid if:
- each **row** contains no duplicate digits  
- each **column** contains no duplicate digits  
- each **3×3 grid** contains no duplicate digits  

Empty cells are represented by `'.'` and ignored during validation.

The algorithm uses three arrays of sets:

- `rowSet[i]` — digits seen in row *i*  
- `colSet[j]` — digits seen in column *j*  
- `gridSet[g]` — digits seen in 3×3 grid *g*, where  
  `g = (i // 3) * 3 + (j // 3)`

As the board is scanned, each digit is checked against its row, column, and grid.  
If a duplicate is found, the board is invalid.

#### Key Details

- Uses constant‑size data structures (9 rows, 9 columns, 9 grids).  
- Runs in **O(1)** time because the board size is fixed (81 cells).  
- Only checks validity; does not solve the puzzle.

## 10_SudokuSolver.py

This file implements a complete backtracking-based solver for a 9×9 Sudoku puzzle.  
The solver fills the board **in-place** and ensures that every placement satisfies:

- row constraints  
- column constraints  
- 3×3 grid constraints  

The algorithm repeatedly locates the next empty cell (`'.'`), tries digits `1–9`, checks validity, and recurses.  
If a placement leads to a contradiction, the solver backtracks and restores the empty cell.

#### Core Components

- **solveSudoku(board)**  
  Entry point. Initiates backtracking and modifies the board directly.

- **backtrack(board)**  
  Searches for the next empty cell, attempts digits, and recurses.  
  Returns `True` when the board is fully solved.

- **isValid(board, r, c, val)**  
  Checks whether placing `val` at `(r, c)` violates any Sudoku rule.

#### Key Details

- Uses depth-first backtracking with constraint checks.  
- Runs in worst-case exponential time, but efficiently solves standard Sudoku puzzles.  
- Modifies the board in-place; no additional data structures required.  
- Ensures correctness by validating row, column, and grid before each placement.
