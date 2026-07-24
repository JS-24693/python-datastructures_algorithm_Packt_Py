#----------------------------
# Declare a new dynamic array
#----------------------------
import array

arr = [1,2] # declare a two-element dynamic array (Python list)

#----------------------------
# Add elements (amortized O(1); occasional resize is O(n))
#----------------------------

# A two‑element list starts with extra capacity, 
# but not necessarily 4.

arr.append(10)   # append O(1) amortized
arr.append(5)    # append O(1) amortized

# resize happens internally when capacity is full (O(n) copy)
arr.append(13)

arr.append(7)    # O(1) amortized

# another resize when needed (O(n) copy)
arr.append(15)

print(arr)   # [1, 2, 10, 5, 13, 7, 15]


#----------------------------
# Create and Access Lists 
# index access = O(1)
# append = amortized O(1) (resize steps are O(n))
#----------------------------

brands = ["Tesla", "Skoda", "Toyota", "Suzuki"]

print(brands)      # ['Tesla', 'Skoda', 'Toyota', 'Suzuki']
print(brands[2])   # access index 2 --> Toyota

# append may trigger a resize if the underlying array is full
brands.append("Volkswagen")
print(brands)      # ["Tesla", "Skoda", "Toyota", "Suzuki", "Volkswagen"]

brands.pop()       # removes last item
print(brands)      # ["Tesla", "Skoda", "Toyota", "Suzuki"]

brands.append("VW")
print(brands)      # ["Tesla", "Skoda", "Toyota", "Suzuki", "VW"]

# Output

# Explicit index-based loop 
# (O(n) because it runs once per element): 
for i in range(len(brands)):
    print(brands[i])

# Direct iteration works same as the for loop
# (also O(n), but simpler and more Pythonic)
for brand in brands:
    print(brand)

# both loops print each element of brands in order
# Tesla
# Skoda
# Toyota
# Suzuki
# VW


#----------------------------
# Sort list (uses O(n log n) time complexity) 
#----------------------------

arr = [10, 5, 13, 7, 15]

arr.sort()
print(arr)            # [5, 7, 10, 13, 15]

arr.sort(reverse=True)
print(arr)            # [15, 13, 10, 7, 5]


# Sort by length of each element (key=len)

# Number of characters in each str element
brands = ["Tesla", "Skoda", "Toyota", "Suzuki", "VW"]

brands.sort(key=len)
print(brands)           # ['VW', 'Tesla', 'Skoda', 'Toyota', 'Suzuki']

# Number of items in each list
listarr = [ [1,2], [1], [1,2,3] ]

listarr.sort(key=len)
print(listarr)          # [[1], [1,2], [1,2,3]]

#----------------------------
# Iteration Methods
#----------------------------

brands = ["Tesla", "Skoda", "Toyota", "Suzuki", "VW"]

# index-based iteration (O(n); more code than needed)
for i in range(len(brands)):
    print(brands[i])

# direct iteration (O(n); simpler and Pythonic)
for brand in brands:
    print(brand)

# both output:
# Tesla
# Skoda
# Toyota
# Suzuki
# VW


#----------------------------
# List Comprehension Basics
#----------------------------

#----------------------------
# Create a list
#----------------------------

# index-based iteration (O(n); more code than needed)
LI = []
for i in range(10):
    LI.append(i)          # append i

# List comprehension (O(n); simpler and Pythonic)
LI2 = [x for x in range(10)]

# Output
print(LI)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(LI2) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#----------------------------
# Applying operations 
#----------------------------

# Example 1: square numbers

# index-based iteration (O(n); more code than needed)
LI = []
for i in range(10):
    LI.append(i*i)

# list comprehension (O(n); simpler and Pythonic)
LI2 = [x*x for x in range(10)]

# Output — both produce squares of 0–9 
print(LI)
print(LI2)

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Example 2: cube of numbers

# index-based iteration (O(n); more code than needed)
LI = []
for i in range(10):
    LI.append(i**3)

# list comprehension (O(n); simpler and Pythonic)
LI2 = [x**3 for x in range(10)]

# Output — both produce cubes of 0–9
print(LI)
print(LI2)

# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]


# Example 3: repeated values
 
# repetion operator (O(n) to allocate n elements)
LI = [5] * 10            # preferred, clean, idiomatic

# list comprehension (O(n); builds list one element at a time)
LI2 = [5 for _ in range(10)] # still valid, but unnecessary here

# Output — both create a list of ten 5s
# both create a list with five value and 10 elements
print(LI)
print(LI2)

# [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
# [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]


#----------------------------
# Creating lists of tuples (1D)
#----------------------------

# explicit nested loops (O(n*m); builds pairs one at a time)
LI = []
for i in range(5):
    for j in range(4):
        LI.append((i, j))

# list comprehension (O(n*m); same work, cleaner syntax)
LI2 = [(i, j) for i in range(5) for j in range(4)]

# Output
print(LI)
print(LI2)

# both generate all (i, j) pairs where:
# i = 0..4 and j = 0..3

# [(0, 0), (0, 1), (0, 2), (0, 3),
# (1, 0), (1, 1), (1, 2), (1, 3),
# (2, 0), (2, 1), (2, 2), (2, 3),
# (3, 0), (3, 1), (3, 2), (3, 3),
# (4, 0), (4, 1), (4, 2), (4, 3)]


#----------------------------
# Adding condition to tuples
#----------------------------

# create tuples where the first number is strictly 
# less than the second are included

# explicit nested loops (O(n*m); condition checked each iteration)
LI = []
for i in range(5):
    for j in range(4):
        if i < j:
            LI.append((i, j))

# list comprehension (O(n*m); same work, cleaner syntax)
LI2 = [(i, j) for i in range(5) for j in range(4) if i < j]

# Output
print(LI)
print(LI2)

# [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
# [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


#----------------------------
# Creating 2D lists
#----------------------------

# create a list containing three other lists 
# with each internal list in the range of 0 - 3

# explicit nested loops (O(n*m); build each inner list element-by-element)
LI = []
for j in range(3):
    inner = []
    for i in range(4):
        inner.append(i)
    LI.append(inner)

# list comprehension (O(n*m); same work, cleaner syntax)
LI2 = [ [ i for i in range(4) ] for j in range(3)]

# Output
print(LI) # [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
print(LI2) # [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]

# both print an inner list of four indexes three times 
# within an outer list


#----------------------------
# Adding condition to 2D loop
#----------------------------

# adding internal lists where i does not equal j
# so remove first index from first inner list, etc.

# explicit nested loops (O(n*m); condition checked each iteration)
LI = []
for j in range(3):
    inner = []
    for i in range(4):
        if i != j:
            inner.append(i)
    LI.append(inner)


# list comprehension (O(n*m); same logic, more concise)
LI2 = [[i for i in range(4) if i != j] for j in range(3)]

# Output
print(LI)  # [[1, 2, 3], [0, 2, 3], [0, 1, 3]]
print(LI2) # [[1, 2, 3], [0, 2, 3], [0, 1, 3]]

# both print each inner list with the indexes removed 
# that would be equal to the j index


#----------------------------
# Slicing
#----------------------------

# base list
LI = [i for i in range(0, 101)]

print(LI) 
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
# ...
# 95, 96, 97, 98, 99, 100]

# explicit loop to collect indexes 0–4 
# (O(k) for k returned items)
LI2 = []
for i in range(0, 5):
    LI2.append(LI[i])
print(LI2)       # [0, 1, 2, 3, 4]

# Slice 0–4 (O(k) for k returned items)
# Each slice runs in O(k) 
# because Python only copies the elements 
# included in the slice.
LI2 = LI[0:5]
print(LI2)       # [0, 1, 2, 3, 4]

# Slice 3–8 (O(k))
LI2 = LI[3:9]
print(LI2)       # [3, 4, 5, 6, 7, 8]

# Slice first 10 elements (O(k))
LI2 = LI[:10]
print(LI2)       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slice last 10 elements (O(k))
LI2= LI[-10:]
print(LI2)       # [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# Slice middle section (O(k))
LI2 = LI[20:40]
print(LI2)      # [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
                # 31, 32, 33, 34, 35, 36, 37, 38, 39]

# explicit loop for every second element from index 3–19 (O(k))
LI2 = []
for i in range(3, 20, 2):
    LI2.append(LI[i])
print(LI2)        # [3, 5, 7, 9, 11, 13, 15, 17, 19]

# Every second element from index 3–19 (O(k))
LI2 = LI[3:20:2]
print(LI2)        # [3, 5, 7, 9, 11, 13, 15, 17, 19]

# Step by 3 across entire list (O(k))
LI2 = LI[::3]
print(LI2)        # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 
                  # 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 
                  # 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 
                  # 93, 96, 99]

# Start at index 5 (O(k))
LI2 = LI[5::]
print(LI2)        # elements from index 5 to 100

# Start at 5, step by 3 (O(k))
LI2 = LI[5::3]
print(LI2)        # [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 
                  # 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 
                  # 71, 74, 77, 80, 83, 86, 89, 92, 95, 98]

# Reverse list (O(k))
LI2 = LI[::-1]
print(LI2)        # prints elements from 100 to 0
