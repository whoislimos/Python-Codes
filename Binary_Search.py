
# Binary Search in Python
# Author: Abdulhalim Yusuf
# Date: November 29th 2015

# Binary Search works with orders lists
def binarySearch(myItem, myList):
    found = False                       # The boolean for the discovered item
    top = len(myList) - 1               # Top limit of the ordered list
    bottom = 0                          # Bottom limit of the ordered list

    while bottom <= top and not found:
        middle = (bottom + top) // 2    # Check the midpoint of the ordered list for the item
        if myList[middle] == myItem:
            found = True

        elif myList[middle] < myItem:
            bottom = middle + 1

        else:
            top = middle - 1

    return found


# binary Search test
number = 100
orderedList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
isItFound = binarySearch(number, orderedList)

if isItFound:
    print "Here's your number"

else:
    print "There is NO such number"
