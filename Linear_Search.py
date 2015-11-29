__author__ = 'amilimos'


# Linear Search

def linearSearch(myitem, myList):
    found = False
    current = 0

    while current < len(myList) and not found:  # limit of size of list and if the item has not been found
        if myList[current] == myitem:  # found the item
            found = True  # assign found variable with True value
        current += 1  # increase by one each iteration

    return found


# Test Case for Linear Search using Mercedes
car = "Mercedes"
brand = ["BMW", "Porshe", "Volkswagen"]

isitFound = linearSearch(car, brand)

if isitFound:
    print ("Your car is in the list of brands.")

else:
    print ("Your car is NOT in the list of brands.")
