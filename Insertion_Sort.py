# Author: Abdulhalim Yusuf
# Date: November 17, 2015
# Project: Insertion Sort

def insertion_sort():

    list_size = len(unsorted)

    for i in range(1, len(unsorted)):

        current = unsorted[i]
        print unsorted[i]
        j = i

        while j > 0 and unsorted[j-1] > current:
            unsorted[j] = unsorted[j-1]
            j = j-1

        unsorted[j] = current

    print "\n"
    print ("The SORTED LIST is: ",unsorted )
    print ('The length of this list is:', len(unsorted))



print "\nHello and welcome to the Insertion Sort test!"
unsorted = [10, 4, 65, 3, 7, 34, 84, 33, 90, 2]
print ("The unsorted list is: ",unsorted )
insertion_sort()
