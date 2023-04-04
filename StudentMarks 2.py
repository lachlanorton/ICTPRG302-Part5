# /////////////////////////////////////////////////////////////
# StudentMarks program
# For ICTPRG302 Assessment Event 2 - Project (Part 5)
#
# Author: Lachlan Orton
# Start Date: 04/04/2023
# Last Updated: 04/04/2023
# On GitHub?: Yes
# TAFE NSW St. Leonard's / ICTPRG302 Programming and Data
#
# This program determines the sum of and average mark for a
# student based on their marks from five different subjects.
# /////////////////////////////////////////////////////////////

import time

print("Please enter your 5 subject marks below:")

# Introduced while loop so that when user inputs incorrect value, it restarts questions.
while True:
    mark1 = input("Enter 1st subject mark: ")
    mark2 = input("Enter 2nd subject mark: ")
    mark3 = input("Enter 3rd subject mark: ")
    mark4 = input("Enter 4th subject mark: ")
    mark5 = input("Enter 5th subject mark: ")

    # Create list with the marks from input
    marksList = [mark1, mark2, mark3, mark4, mark5]
    # Created empty list for valid marks, this will be used to calculate sum and avg.
    calculateMarks = []
    # Using for loop, check if each entry in marksList is a integer
    for entry in marksList:
        if entry.isdigit():
            # If it is an integer, cast to new variable
            value = int(entry)
            # Check to see if this integer is 0 or more and 100 or less.
            if value < 0 or value > 100:
                # If value is not valid, break out of for loop
                print("\nYou entered:", entry, "\nThis is not a valid mark. Please enter a valid mark.\n")
                time.sleep(2)
            # If value is valid, add the value to the newly created list
            calculateMarks.append(value)
        else:
            # If entry is not even a digit, break out of for loop
            print("\nYou entered:", entry, "\nThis is not a valid mark. Please enter a valid mark.\n")
            time.sleep(2)
    # Check to see if calculateMarks list length matches 5 (matches how many subjects required)
    if len(calculateMarks) >= 5:
        # If it matches, then leave while loop and continue with program
        break

# Print the list
print("\nYou entered the following marks:")
print(*calculateMarks, sep=", ")

# Calculate the sum and average
sumOfMarks = sum(calculateMarks)
averageOfMarks = sum(calculateMarks)/5

# Display results
time.sleep(2)
print("\nThe sum of your marks is: "+str(sumOfMarks))
print("The average of your marks is: "+str(averageOfMarks))
