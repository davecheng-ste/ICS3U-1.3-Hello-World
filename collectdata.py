"""
File: collectdata.py
Author: Dave Cheng
Date: 2024-02-20
Description: Collects user data and outputs results.
"""

# Get inputs from user
str_name_first = input("Enter your first name: ")
str_name_last = input("Enter your last name: ")
num_age = int(input("Enter your age: "))
float_mark = float(input("Enter your current mark: "))
has_locker = input("Have you been assigned a locker (True/False)? ")

# Output formatted results
print("Name: " + str_name_first + " " + str_name_last)
print("Age:", num_age)
print("Current Mark:", float_mark)
print("Locker Assigned:", has_locker)
