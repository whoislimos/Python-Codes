''' Quick Sort   '''

def quickSort(given_list):
    less = []
    pivotList = []
    more = []
    if len(given_list) <= 1:
        return given_list
    else:
        pivot = given_list[0]

        for i in given_list:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        less = quickSort(less)
        more = quickSort(more)

        return less + pivotList + more

#test case
unsorted = [40, 63, 2, -39, 10, 67, 908, 321, 2]
print quickSort(unsorted)
