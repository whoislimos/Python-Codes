# Author: Abdulhalim Yusuf
# Date: November 12, 2015
# Project: Bubble Sort


#list = [3 , 2, 9 , 6 , 5]
list =[23 ,42 ,4 ,16 ,8 ,15]

print ("==== Bubble Sort Test begins ====\n")

print ("Unsorted List", (list))

print ("The length of this list is", (len(list)), "\n")



for j in range ((len(list)-1), 0, -1):
        
    for i in range(j):
    
    	if (list[i] > list[i+1]):
    		
    		temp = list[i]
    		list[i] = list[i+1]
    		list[i+1] = temp
    		
    	print ("Every List", (list))
		
		
print ("\nSorted List", (list))
print ("\n==== Program End after printing ====")		
	
	
