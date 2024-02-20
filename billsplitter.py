"""
File: billsplitter.py
Author: Dave Cheng
Date: 2024-02-20
Description: Calculates how much each person in a group should pay based on a group meal's total 
             bill after-tax. Assumes 13% HST on total bill. Calculates tip on pre-tax amount.
"""

print("Restaurant Bill Splitter\n")

# Ask the user for input
group_size = input("How many people in your group? ")
aftertax_total = input("What was the total bill after tax? ")
tip_percentage = input("How much do you want to tip (standard is 15%)? ")

# Calculate pre-tax total by backing out HST from after-tax total
pretax_total = float(aftertax_total) / 1.13

# Calculate desired tip based on pre-tax total
tip_total = pretax_total * (float(tip_percentage) / 100)

# Add tip and after-tax total for final amount owing by the group
total_payable = float(aftertax_total) + tip_total

# Calculate individual part of the group total, rounded
individual_payable = round(total_payable / int(group_size), 2)

# Output result to user
print("\nEach person should pay $", individual_payable)
