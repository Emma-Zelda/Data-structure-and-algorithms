# Examples
"""
Description: Examples from Data Structures & Algorithms course on Udacity
Created on Tue Apr 30
@author: Emma.Teng
"""

"""
1. Introduction
"""
# Lesson 2 Python Refresher

# Exercise 1: Generate factorials
# Create a generator fact_gen() that generates factorials. In this exercise,
#   we will define prod(a, b) which returns the product of numbers a and b,
#   and fact_gen() which yields the next factorial number.
def prod(a,b):
    # TODO change output to the product of a and b
    output = a * b
    return output

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        # TODO: update i and n
        i += 1
        n = output
        # Hint: i is a successive integer and n is the previous product


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120


# Exercise 2: Check sudoku squares for correctness
    
# A valid sudoku square satisfies these two properties:
#    1.Each column of the square contains each of the whole numbers 
#       from 1 to n exactly once.
#   2. Each row of the square contains each of the whole numbers 
#       from 1 to n exactly once.

def check_sudoku(square):
    for row in square:
        # Create a list with the integers 1, 2, ..., n.
        # We will check that each number in the row is in the list
        # and remove the numbers from the list once they are verified
        # to ensure that each number only occurs once in the row.
        check_list = list(range(1, len(square[0]) + 1))
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i) 
    for n in range(len(square[0])):
        # We do the same here for each column in the square.
        check_list = list(range(1, len(square[0]) + 1))
        for row in square:
            if row[n] not in check_list:
                return False
            check_list.remove(row[n])
    return True

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

print(check_sudoku(incorrect)) #>>> False
print(check_sudoku(correct)) #>>> True
print(check_sudoku(incorrect2)) #>>> False
print(check_sudoku(incorrect3)) #>>> False
print(check_sudoku(incorrect4)) #>>> False








