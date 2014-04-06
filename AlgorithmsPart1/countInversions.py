#Count inversions (valuepair (i,j), where i<j and A[i]>A[j]) algorithm
###########################
#Input: unsorted list of non-reoccuring elements, usually ranking data
#Idea: use the merge-sort-algorithm and count the inversions when merging as a byproduct


def sortAndCount(unsortedList):
#sortAndCount(array, length)
    listLength = len(unsortedList)
    #divide the array in half recursively
    if listLength == 1:
	#until the length is 1, return 0 number of recursion,  array
	return 0, unsortedList
    
    #call self recursively with left half
    (lefRec,sortedLeftHalf) = sortAndCount (unsortedList[0:listLength/2])

    #call self recursively with right half
    (rigRec,sortedRightHalf) = sortAndCount (unsortedList[listLength/2:])

    #mergeCountInv(), take the sorted left and right halfs 
    (merRec,mergedList) = mergeCountInv(sortedLeftHalf,sortedRightHalf)
    	   
    #add all the partial results and return merged and sorted halfs
    return (lefRec + rigRec + merRec),mergedList

	
def mergeCountInv(leftHalf,rightHalf):
    """sort the left and right half back together, and count the inversions while doing so, by counting the remaining elements in the left array whenever copying an elment from the right array"""
    #set a counter to the leftmost element of both input arrays and copy the smallest value into a new array (growing to be the merged version of those two)
    lP,rP,merRec = 0,0,0 
    sortedList=[]
    while (len(sortedList) <len(rightHalf)+len(leftHalf)):
	if  rP == len(rightHalf) or\
	    lP < len(leftHalf) and \
	    leftHalf[lP]<= rightHalf[rP]:
	    #if already copied all the elements from the right, just copied the current left element, otherwise check if all the elements are already copied from the left before comparing current left and right elements
	    sortedList.append(leftHalf[lP])
	    lP +=1
	elif lP == len(leftHalf) or\
	    rP < len(rightHalf) and\
	    rP < len(rightHalf):
	    sortedList.append(rightHalf[rP])
	    rP +=1
	    merRec += len(leftHalf[lP:len(leftHalf)])
    return merRec, sortedList

#open file and read data into an array
unsortedList = []
arrayFile = open("countInversionsInput.txt","r")
for line in arrayFile.readlines():
    unsortedList.append(int(line.rstrip()))
inversions, sortedList=sortAndCount(unsortedList)
print("Sorted list:%s \n Inversions:%s"%(str(sortedList),inversions))
