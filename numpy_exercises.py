import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1) How many negative numbers are there?
# Evaluates each element in the array to see if is less than 0 and then counts the number of times that is true 
print(np.sum(a < 0))

# 2) How many positive numbers are there?
# Evaluates each element in the array to see if is greater than 0 and then counts the number of times that is true 
print(np.sum(a > 0))

# 3) How many even positive numbers are there?
# Evaluates each element in the array to see if each one has a remainder of 0 for % 2 and then counts the number of times it is true
print(np.sum(a % 2 == 0 ))

# 4) If you were to add 3 to each data point, how many positive numbers would there be?
# Adds 3 to each element and then counts the number of the trasnformed elements that evaluate to x > 0
print(np.sum(a + 3 > 0))

# 5) If you squared each number, what would the new mean and standard deviation be?
# - Method 1

# Squares each element and then finds the mean for the whole arrary
print(f"The new mean would be {np.mean(a**2)}")
# Squares each element and then finds the stanardard deviation for the whole arrary
print(f"The new stanard deviation would be {np.std(a**2)}")

# - Method 2
# Each element is multiplied itself and then assgined to a varaiable new_5
new_5 = a ** 2

# Finds the mean of new_5
print(f"The new mean would be {new_5.mean()}")
# Finds the standard deviation for new_5
print(f"The new standard deviation would be {new_5.std()}")


# 6) A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. 
# This is done by subtracting the mean from each data point. Center the data set.

# Find the mean of the whle arrary and then subtracts the mean from each element to get and prints the results
print(a - (np.mean(a)))


# 7) Calculate the z-score for each data point
# Uses the numpy's mean and standard deviation functions and then finds the z score 
print((a - a.mean())/a.std())

# 8) Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
# Sums all the numbers in list a
sum_of_a = sum(a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
# Finds the smallest number in list a
min_of_a = min(a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
# Finds the biggest number in list a
max_of_a = max(a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
# Sums all the numbers in list a and then divides by the number of numbers in list a
mean_of_a = sum(a)/len(a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# Creates a function to multiply each number of a list by the next next number in the list.
def product(mylist):
    p = 1
    for x in mylist:
        p *= x
    return p

# uses the function to then calculate the product of a
product_of_a = product(a)    
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [x**2 for x in a]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
# Uses list comprehension to pull all the odd numbers in list a
odds_in_a = [x for x in a if x % 2 != 0]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
# Uses list comprehension to pull all the even numbers in list a
evens_in_a = [x for x in a if x % 2 == 0]

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

# convert b to a numpy arrary
b = np.array(b)

# Use the numpy sum function to find the total of an array 
sum_of_b = b.sum()

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

# Use the numpy's variable.min function to find the smallest value in array b
min_of_b = b.min()

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

# Use numpy's variable.max function to find the largest number in array b
max_of_b = b.max()

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

# Use numpy's variable.mean function to find the average of array b
mean_of_b = b.mean()

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
# Use numpy's variable.prod function to find the product of array b
b.prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

# Since B is a numpy array you can just do b ** 2 to get each element squared 
squares_of_b = b ** 2


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

# Uses numpy's reference ability to extract all elements in b where b % 2 does not equal 0 (odds)
odds_in_b = b[b % 2 != 0]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

# Uses numpy's reference ability to extract all elements in b where b % 2 does equal 0 (evens)
evens_in_b = b[b % 2 == 0]

# Exercise 9 - print out the shape of the array b.

print(b.shape)

# Exercise 10 - transpose the array b.

print(b.transpose())

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
print(b.reshape(1, 6))


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
print(b.reshape(6, 1))

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
c = np.array(c)

# Exercise 1 - Find the min, max, sum, and product of c.
# Use variable. min, max, sum, and product to find the answers
print(c.min())
print(c.max())
print(c.sum())
print(c.prod())

# Exercise 2 - Determine the standard deviation of c.
print(c.std())

# Exercise 3 - Determine the variance of c.
print(c.var())

# Exercise 4 - Print out the shape of the array c
print(c.shape)

# Exercise 5 - Transpose c and print out transposed result.
print(c.transpose())

# Exercise 6 - Get the dot product of the array c with c. 
# Use numpy's dot functon
print(c.dot(c))

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# why this work
print(sum(sum(c * c.transpose())))

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

print((c * c.transpose()).prod())



## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d
print(np.sin(d))

# Exercise 2 - Find the cosine of all the numbers in d
print(np.cos(d))

# Exercise 3 - Find the tangent of all the numbers in d
print(np.tan(d))

# Exercise 4 - Find all the negative numbers in d
print(d[d < 0])

# Exercise 5 - Find all the positive numbers in d
print((d[d > 0]))

# Exercise 6 - Return an array of only the unique numbers in d.
print(np.unique(d))

# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))

# Exercise 8 - Print out the shape of d.
print(d.shape)

# Exercise 9 - Transpose and then print out the shape of d.
print((d.transpose()).shape)

# Exercise 10 - Reshape d into an array of 9 x 2
print(d.reshape(9, 2))