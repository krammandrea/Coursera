#Quicksort Algorithm using the first element in each array as the pivot
#Programming Assignement question 1: count the number of comparisons during each iteration with m-1
#Input: unsorted list of integers as .txt
#Idea: choose a pivot element and swap elements into a smallerThan and largerThan part of the array, resulting in moving the pivot element into it's designated spot; recurse


#Partition(Array, leftEnd, rightEnd)
def partition(array, leftEnd, rightEnd,comparisonCounter):

    print(rightEnd - leftEnd)

    #if nothing more left to sort, return
    if rightEnd - leftEnd <= 1:
	return comparisonCounter

    #add length of array -1 to the comparison counter; see assignment 1
    comparisonCounter += rightEnd - leftEnd -1

    #set the rightmost element as the pivot, and move it to the rightmost position
    array[leftEnd],array[rightEnd-1] = array[rightEnd-1],array[leftEnd]
    pivotElement = array[leftEnd]

    #firstLargerThan marker
    firstLargerThan = leftEnd +1

    #iterate newestUnpartitioned marker over all the elements in the array
    for newestUnpartitioned in range(leftEnd +1,rightEnd):
	
	#if nU smaller than pivot element 
	if array[newestUnpartitioned] < pivotElement:
	    #swap nU with firstLargerThan
	    array[newestUnpartitioned],array[firstLargerThan] =\
		array[firstLargerThan],array[newestUnpartitioned]
	    #move firstLargerThan marker one to the right
	    firstLargerThan += 1

    #swap pivot and lastSmallerThan (=firstLargerThan -1)
    pivotPosition = firstLargerThan -1 
    array[leftEnd],array[pivotPosition] = array[pivotPosition],array[leftEnd]

    #recursively call smallerThan and largerThan part of the array
    comparisonCounter = partition(array,leftEnd,pivotPosition,comparisonCounter) 
    comparisonCounter = partition(array,pivotPosition +1,rightEnd,comparisonCounter)

    #return comparisonCounter
    return comparisonCounter


#read input file numbers, unsorted, QuickSortInput
unsortedList = []
arrayFile = open("QuickSortInput.txt","r")
for line in arrayFile.readlines():
    unsortedList.append(int(line.rstrip()))
arrayFile.close()

comparisonCounter =0
comparisonCounter = partition(unsortedList,0,len(unsortedList),comparisonCounter)

print("%s"%str(unsortedList))
print("Accumulated Comparisons %s"%str(comparisonCounter))



