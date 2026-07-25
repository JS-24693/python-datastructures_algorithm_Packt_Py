# Foundations of Data Structures & Algorithms in Python Course - Packt

## S03 - ArraysandLists Folder

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

## S04 - Sorting Folder

## 01_bubblesort.py

#### AlgorithmConceptualUnderstanding Class

This module provides a minimal, instructional implementation of the bubble sort algorithm. 

Bubble sort is a comparison‑based, in‑place sorting method that repeatedly scans the list, compares adjacent elements, and swaps them when out of order. Each pass pushes the largest remaining element to its correct position, shrinking the unsorted region.

## 02_selectionsort.py

This module implements the selection sort algorithm. Selection sort scans the unsorted portion of the list, finds the smallest element, and swaps it into its correct position. After each pass, the sorted region grows by one element.

#### selection_sort(li)

Performs an in-place selection sort.

- Outer loop selects index `i` where the next smallest element should be placed.
- Inner loop scans `li[i:]` to find the smallest element.
- Swap places the smallest element at index `i`.
- Time complexity: O(n^2).

## 03_insertionsort.py

This module provides a minimal, instructional implementation of insertion sort.
Insertion sort builds a sorted region one element at a time. The element at index 0 is treated as sorted; each subsequent element (key = li[i]) is inserted into its correct position by shifting larger elements to the right.

Insertion sort is adaptive:
- Best case (already sorted): inner loop performs no shifts → O(n)
- Worst case (reverse sorted): each key shifts across entire sorted region → O(n²)

## 04_mergetwosortedarrays.py

This module implements the merge operation used in merge sort.  
Given two sorted arrays `A` and `B`, the function `merge_sorted_arrays(A, B)` produces a new sorted array `C` containing all elements from both inputs.

#### Algorithm

The merge procedure uses two pointers:
- `i` — current index in `A`
- `j` — current index in `B`

At each step, the smaller of `A[i]` and `B[j]` is appended to `C`.  
When one array is exhausted, the remaining elements of the other array are appended directly.

This guarantees linear time:
- Each iteration advances either `i` or `j`
- Total operations = `n + m`
- Time complexity: **O(n + m)**

## 05_divideconquer.py

This module implements merge sort using a divide-and-conquer strategy.
The algorithm recursively divides the array into two halves until each
subarray has size 1, then merges sorted halves using the merge operation.

#### Algorithm Overview

1. **Divide**
   - Compute midpoint: `mid = (left + right) // 2`
   - Recursively sort `left..mid`
   - Recursively sort `mid+1..right`

2. **Conquer**
   - Merge the two sorted halves using a temporary array `C`
   - Copy merged results back into the original array

#### Complexity

- **Time:** O(n log n)
- **Space:** O(n)
- Merge sort guarantees n log n performance for all inputs.

## 06_quicksort.py

This module implements the partitioning step used in quicksort.
Partitioning rearranges an array around a pivot so that:

- All elements <= pivot appear on the left
- Pivot appears in its correct final position
- All elements > pivot appear on the right

Partitioning does **not** sort the array; it only groups elements
relative to the pivot. Quicksort uses this operation recursively
to sort the left and right subarrays.

#### Algorithm

1. Choose pivot as the last element.
2. Initialize `left = -1`.
3. Scan from index `0` to `n-2`:
   - If `A[i] <= pivot`, increment `left` and swap `A[i]` with `A[left]`.
4. After scanning, increment `left` and swap pivot into position `left`.

#### Complexity

- **Time:** O(n)
- **Space:** O(1)

## 07_countingsort.py

Counting sort is a non-comparison-based sorting algorithm that achieves
linear time complexity O(n + m), where n is the number of elements and m
is the maximum value in the array.

It works by counting occurrences of each value, building a cumulative
frequency array, and placing each element into its correct sorted
position. Counting sort is stable and is used inside radix sort.

#### Algorithm Steps

1. Find the maximum value in the array.
2. Build a frequency array of size (max_value + 1).
3. Convert frequency array to cumulative frequency.
4. Traverse the array in reverse to ensure stability.
5. Place each element into its correct sorted position.
6. Copy the result back into the original array.

#### Complexity

- **Time:** O(n + m)
- **Space:** O(n + m)
- **Stable:** Yes
- **Comparison-based:** No

## 08_move_zeroes.py

The Move Zeroes (LeetCode 283) algorithm moves all zeros in an array to the end while preserving the relative order of non-zero elements. It uses a partition-style approach similar to quicksort.

#### Algorithm

1. Maintain a pointer `start` for the next non-zero placement.
2. Scan the array from left to right.
3. When a non-zero element is found:
   - Swap it with `nums[start]`
   - Increment `start`
4. Zeros naturally shift to the end.

#### Complexity

- **Time:** O(n)
- **Space:** O(1)
- **Stable:** Yes (non-zero order preserved)

## 09_majority_element.py

#### Majority Element — Moore's Voting Algorithm (LeetCode 169)

This solution finds the majority element in O(n) time and O(1) space
using Moore's Voting Algorithm. The majority element is guaranteed to
exist and appears more than n/2 times.

#### Algorithm

1. Choose the first element as the candidate.
2. Set count = 1.
3. For each element:
   - If it matches the candidate, increment count.
   - Otherwise, decrement count.
   - If count becomes 0, choose a new candidate and reset count to 1.
4. The final candidate is the majority element.

#### Complexity

- **Time:** O(n)
- **Space:** O(1)

## 10_sort colors.py

The Sort Colors — Dutch National Flag Algorithm (LeetCode #75) problem requires sorting an array containing only 0, 1, and 2 without using built-in sorting. 
The optimal solution is the Dutch National Flag algorithm, which partitions the array in a single pass.

#### Algorithm

Use three pointers:
- `left`  → next position for a 0
- `right` → next position for a 2
- `i`     → current index

Rules:
1. If nums[i] == 0: swap with nums[left], increment both left and i.
2. If nums[i] == 2: swap with nums[right], decrement right only.
3. If nums[i] == 1: increment i.

#### Complexity

- **Time:** O(n)
- **Space:** O(1)

## S05 - Linked Lists Folder 
