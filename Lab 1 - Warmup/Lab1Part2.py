"""
Part 2: List of classes

Write a program that asks for the names of all of the classes you are taking this semester
    Save these class names in a list.
    Print all the items in the list, one per line.
"""

classList = []

newEntry = True

print("Enter the names of the classes you are taking one by one, "
      "press enter after each and leave blank when finished.")
while newEntry:
    newClass = input("Enter class name: \n")
    if newClass == "":
        newEntry = False
    classList.append(newClass)

for each in classList:
    print(each)
