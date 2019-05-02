"""
                Lesson_3_How_to_solve_problems.py
Description: Examples from Data Structures & Algorithms course on Udacity
    Lesson 3: How to solve problems
Last Modified on: May 02, 2019
@author: Emma.Teng
"""

"""
Days between Dates:
    Calculate the number of days between two dates.
        Be ware of leap years.
"""
"""
Algorithm pseudocode:
    days = # of days in month1 - day1 eg: 31-24 = 7
    month1 += 1
    while month1 < month2:
        days += # of days in month1
        month1 += 1
    days += day2
    
    while year1 < year2:
        days += days in year1

The above code is not good enough for implementation, because 
it doesn't handle:
    - input dates in same month
    - month2 < month 1, year2 > year1
    - counting days for leap years
"""

"""
A simpler mechanical algorithm:
    days = 0
    while date1 is before date2:
        date1 = advance to next day
        days += 1

Too slow...

"""


















