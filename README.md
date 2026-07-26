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

The pivot position directly determines recursion depth: 
• If the pivot lands near the middle, recursion is balanced and fast. 
• If the pivot lands near an end, recursion becomes unbalanced and slower. 

This pivot dependent splitting is what creates quicksort’s three major time complexity behaviors: Best Case — O(n log n), Occurs when each pivot divides the array into two nearly equal halves. Average Case — O(n log n), Random data typically produces reasonably balanced partitions. Worst Case — O(n²), Occurs when each pivot produces extremely unbalanced partitions (e.g., already sorted input with a poor pivot choice). 

As far as Space Complexity: Best & Average Case — O(log n), Balanced partitions produce a recursion depth of log n, so the call stack stores log n frames. Worst Case — O(n), Unbalanced partitions produce a recursion depth of n, so the call stack grows linearly.

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

## 01_linkedlist_basic.py

The Singly Linked List — Basic Manual Implementation project demonstrates a minimal singly linked list in Python.

#### Concepts
- A **node** stores `data` and a `next` pointer.
- A **linked list** is a chain of nodes connected by `.next`.
- The **head** pointer identifies the first node.
- Traversal follows `.next` until reaching `None`.

#### File: linkedlist_basic.py
- Defines a `Node` class.
- Manually constructs nodes A → B → C → D.
- Traverses and prints the list.

## 02_linkedlist_insert_top.py

The Linked List — Insert at Top (Front) project demonstrates how to dynamically insert nodes at the front of a
singly linked list in Python.

#### Concepts
- A **node** stores `data` and `next`.
- **insert_at_top(data)** makes the new node the head.
- Pointer update: `NN.next = head` then `head = NN`.
- Empty list: new node becomes head.

#### File: linkedlist_insert_top.py
- Defines `Node` class.
- Implements `insert_at_top` and `traverse`.
- Test sequence inserts A, B, E, C → prints C, E, B, A.


## 03_linkedlist_insert_end.py 

The Linked List — Insert at End project demonstrates how to dynamically insert nodes at the end of a singly linked list in Python.

#### Concepts
- A **node** stores `data` and `next`.
- **insert_at_end(data)** traverses to the last node and attaches the new node.
- Empty list: new node becomes head.
- Traversal stops when `current.next` is `None`.

#### File: linkedlist_insert_end.py
- Defines `Node` class.
- Implements `insert_at_end` and `traverse`.
- Test sequence inserts A, B, C, D at end, then Z at top → prints Z, A, B, C, D.

## 04_linkedlist_insert_middle.py

The Linked List — Insert in Middle project demonstrates how to insert nodes at arbitrary positions in a singly linked list.

#### Concepts
- To insert at position `pos`, traverse to `pos-1`.
- Rewire pointers:
  - `NN.next = current.next`
  - `current.next = NN`
- Empty list → new node becomes head.
- Position too large → insert at end.

#### File: linkedlist_insert_middle.py
- Defines `Node` class.
- Implements `insert_at` and `traverse`.
- Test sequence builds A B C D, then inserts Z at pos 2, X at pos 1, Y at pos 100.

## 05_linkedlist_delete_top.py 

The Linked List — Delete at Top project demonstrates how to delete the first node of a singly linked list.

#### Concepts
- Deleting at top means updating `head` to `head.next`.
- Removed node becomes unreachable and is garbage collected.
- Empty list → no deletion performed.
- Time complexity: O(1).

#### File: linkedlist_delete_top.py
- Defines `Node` class.
- Implements `delete_at_top` and `traverse`.
- Test sequence builds A B C D E, deletes twice, and prints results.

## 06_linkedlist_delete_end.py

The Linked List — Delete at End project demonstrates how to delete the last node of a singly linked list.

#### Concepts
- To delete the last node, traverse to the second-last node.
- Update: `second_last.next = None`.
- Single-node list → `head = None`.
- Time complexity: O(n) due to traversal.

#### File: linkedlist_delete_end.py
- Defines `Node` class.
- Implements `delete_at_end` and `traverse`.
- Test sequence builds A B C D E, deletes twice, and prints results.

## 07_intersection_linkedlists.py

The Intersection of Two Linked Lists project implements the optimal O(M+N), O(1)-space algorithm for finding the intersection node of two singly linked lists.

#### Key Idea
After the intersection point, both lists share the same tail length. Align
the pointers by advancing the longer list's pointer, then walk both pointers
together until they meet.

#### Steps
1. Compute lengths of both lists.
2. Advance pointer in longer list by the length difference.
3. Move both pointers forward together.
4. First node where they match is the intersection.

#### File: intersection_linkedlists.py
- Defines `Node`
- Implements `length` and `get_intersection`
- Includes a test case demonstrating intersection at C1.

## 08_merge_sorted_lists.py

The Merge Two Sorted Linked Lists project implements the optimal O(m+n), O(1)-space algorithm for merging two sorted singly linked lists.

#### Key Idea
Use two pointers to walk through both lists, always choosing the smaller
value to append. When one list finishes, append the remainder of the other.

#### Steps
1. Initialize pointers p1 and p2 at heads of both lists.
2. Compare values and append the smaller node.
3. Advance the pointer whose node was used.
4. Append remaining nodes when one list ends.
5. Return the merged list’s head.

## 09_linkedlist_cycle.py

The Linked List Cycle Detection project implements Floyd's Tortoise and Hare algorithm to detect cycles in a singly linked list.

#### Key Idea
Use two pointers moving at different speeds. If they ever meet, the list
contains a cycle. If the fast pointer reaches None, the list is acyclic.

#### Steps
1. Handle edge cases (0 or 1 nodes).
2. Initialize slow = head, fast = head.next.
3. Move slow by 1 step, fast by 2 steps.
4. If slow == fast → cycle detected.
5. If fast reaches None → no cycle.

## 10_reverse_linkedlist_recursive.py

The Reverse Linked List (Recursive) project implements the recursive algorithm for reversing a singly
linked list.

#### Key Idea
Define a recursive function that reverses the list from the current node
onward. The last node becomes the new head. As recursion unwinds, pointers
are rewired so each node points backward.

#### Steps
1. Base case: if node.next is None → new head = node.
2. Recursive call: last = reverse(node.next)
3. Rewire: last.next = node
4. After recursion: original head.next = None
5. Return new head

## 11_palindrome_linkedlist.py

Palindrome Linked List (O(n) time, O(1) space) implements the optimal algorithm for checking whether a singly linked list is a palindrome without using extra space.

#### Key Idea
Reverse the second half of the list in-place, then compare both halves.

#### Steps
1. Compute list length.
2. Determine reverse start index:
   - Even: n/2
   - Odd: n/2 + 1
3. Reverse second half iteratively.
4. Compare first half and reversed second half.
5. Return True if all values match.

## 12_linkedlist_cycle_start.py

The Linked List Cycle Start project extends Floyd’s Tortoise and Hare algorithm to not only detect a cycle in a singly linked list, but also locate the exact node where the cycle begins.

#### Key Idea

Use two pointers moving at different speeds to detect a cycle.
Once they meet, reset one pointer to the head and move both one step at a time.
The node where they meet again is the cycle entry point.

#### Steps

- Detect the cycle using slow and fast pointers.
- If fast reaches None, the list has no cycle.
- When slow and fast meet, a cycle exists.
- Reset one pointer to head.
- Move both pointers one step at a time.
- The node where they meet is the cycle start.

#### Complexity

- Time: O(n) — you traverse the list at most twice, so work grows linearly with list size.
- Space: O(1) — you use only a few pointers, no extra data structures.

## 13_find_middle_linkedlist.py

The Find Middle of Linked List project implements the optimal slow–fast pointer method to find the middle node of a singly linked list in one pass.

#### Key Idea
Move slow by 1 step and fast by 2 steps. When fast reaches the end, slow
will be at the middle.

#### Even-Length Lists
Return the second middle (e.g., list of length 6 → return node 4).

## 14_add_two_numbers.py

Add Two Numbers (Linked List) represented as reversed linked lists.

#### Key Idea
Traverse both lists, add digit-by-digit with carry, and build a new list
containing the result digits in reversed order.

#### Steps
1. Initialize carry = 0.
2. Loop while either list has digits.
3. Sum digits + carry.
4. Create new node with sum % 10.
5. Update carry = sum // 10.
6. Append final carry if needed.

## 15_remove_nth_from_end.py

The Remove Nth Node from End of List (One-Pass) project implements the optimal O(n) / O(1)-space algorithm for removing the Nth node from the end of a singly linked list.

#### Key Idea
Move fast pointer N+1 steps ahead. Then move both pointers together until
fast reaches None. Slow will be just before the node to delete.

#### Steps
1. Move fast pointer N+1 steps.
2. If fast becomes None early → delete head.
3. Move slow and fast together.
4. Rewire slow.next to skip the target node.
5. Return updated head.
