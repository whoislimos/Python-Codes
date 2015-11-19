# Author: Abdulhalim Yusuf
# Date: November 17, 2015
# Project: Selection Sort



def selectionSort(a):
	n = len(a)
	for i in range(0,n):
		k = i
		for j in range (i+1,n):
			if a[j] < a[k]:
				k = j
		a[i], a[k] = a[k], a[i]
