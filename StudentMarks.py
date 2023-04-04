print("Welcome to the Student Marks program.")
print("Please enter your 5 subject marks below.")


def markinput():
    mark1 = input("Enter 1st subject mark: ")
    mark2 = input("Enter 2nd subject mark: ")
    mark3 = input("Enter 3rd subject mark: ")
    mark4 = input("Enter 4th subject mark: ")
    mark5 = input("Enter 5th subject mark: ")
    return (mark1, mark2, mark3, mark4, mark5)


def markcheck():


# create list with five marks
marksList = [mark1, mark2, mark3, mark4, mark5]

for entry in marksList:
    if entry.isdigit():
        entry = int(entry)
        continue
    else:
        print(entry, " is NOT a digit!")
        break

# print the list
# print("You have entered the following marks:")
# print(*marksList, sep=", ")
#
# # calculate the sum and average
# sumOfMarks = sum(marksList)
# averageOfMarks = sum(marksList) / 5
#
# # Display results
# print("\nThe sum of your marks is: " + str(sumOfMarks))
# print("The average of your marks is: " + str(averageOfMarks))
