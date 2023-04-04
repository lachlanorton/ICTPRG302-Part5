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

while True:
    mark1 = input("Enter 1st subject mark: ")
    mark2 = input("Enter 2nd subject mark: ")
    mark3 = input("Enter 3rd subject mark: ")
    mark4 = input("Enter 4th subject mark: ")
    mark5 = input("Enter 5th subject mark: ")

    # create array/list with five marks
    marksList = [mark1, mark2, mark3, mark4, mark5]
    calculateMarks = []
    for entry in marksList:
        if entry.isdigit():
            value = int(entry)
            if value < 0 or value > 100:
                print("\nYou entered:", entry, "\nThis is not a valid mark. Please enter a valid mark.\n")
                time.sleep(2)
                break
            calculateMarks.append(value)
        else:
            print("\nYou entered:", entry, "\nThis is not a valid mark. Please enter a valid mark.\n")
            time.sleep(2)
            break
    if len(calculateMarks) >= 5:
        break

# print the array/list
print("\nYou entered the following marks:")
print(*calculateMarks, sep=", ")

# calculate the sum and average
sumOfMarks = sum(calculateMarks)
averageOfMarks = sum(calculateMarks)/5

# display results
time.sleep(2)
print("\nThe sum of your marks is: "+str(sumOfMarks))
print("The average of your marks is: "+str(averageOfMarks))
