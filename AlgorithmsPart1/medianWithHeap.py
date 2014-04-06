#Input: a stream of numbers added over time
#Output: median of all numbers so far, during every time 
#Idea: maintain two heaps of equal size, median is either at the root of 
#max-heap or min-heap

class MinHeap(object):
    """
    heap represented in an array, root contains the minimum, add element and 
    remove root supported
    """
    def __init__(self):
	self.elements = []
    def __len__(self):
	return len(self.elements)
    
    def parent(self,i):
	if i == 0:
	    return None
	else:
	    return ((i+1)//2)-1
    def smallestChild(self,i):
	#no children exist
	if (2*i)+1 >= len(self):
	    return None
	#only one child exists
	elif (2*i)+2 >= len(self):
	    return (2*i)+1
	#find the smaller of two children
	elif self.elements[(2*i)+1] < self.elements[(2*i)+2]:
	    return (2*i)+1
	else:
	    return (2*i)+2
    def addElement(self,element):
	self.elements.append(element)
	self.bubbleUp(toBubbleUp = len(self.elements)-1)
    def bubbleUp(self,toBubbleUp):
	parent = self.parent(toBubbleUp)
        while parent != None  and\
              self.elements[toBubbleUp] < self.elements[parent]:
            self.swap(toBubbleUp,parent)
            toBubbleUp = parent
	    parent = self.parent(toBubbleUp)
    def bubbleDown(self,toBubbleDown):
	smallestChild = self.smallestChild(toBubbleDown)
        while smallestChild != None and\
	      self.elements[toBubbleDown] > self.elements[smallestChild]:
	    self.swap(toBubbleDown,smallestChild)
            toBubbleDown = smallestChild
	    smallestChild = self.smallestChild(toBubbleDown)
    def swap(self, i, j):
	self.elements[i],self.elements[j] = self.elements[j],self.elements[i]
    def __str__(self):
	import math
	representation = str("Heap:")	
	#calculate newline to present a binary tree
	powerOfTwo = [int(math.pow(2,k)) for k in range(0,7)]
	newLine = [sum(powerOfTwo[0:x])for x in range(0,len(powerOfTwo))]
	for e in range(0,62):
	    if e in newLine:
		representation +="\n"
	    representation += (str(self.elements[e]))
	    representation +=" "
	return representation
    def popRoot(self):
	self.swap(0,-1)
	#remove root from heap before rearangeing 
	heapRoot = self.elements.pop(-1)
	self.bubbleDown(toBubbleDown = 0)
	return heapRoot	
	
class MaxHeap (MinHeap):
    """
    heap represented in an array, root contains the maximum, add element and 
    remove root supported
    """	
    def __init__(self):
	self.elements = []
    def bubbleUp(self,toBubbleUp):
        while toBubbleUp > 0 and\
              self.elements[toBubbleUp] > self.elements[self.parent(toBubbleUp)]:
            self.swap(toBubbleUp,self.parent(toBubbleUp))
            toBubbleUp = self.parent(toBubbleUp)
    def bubbleDown(self,toBubbleDown):
	largerChild = self.largerChild(toBubbleDown)
        while largerChild != None and\
	      self.elements[toBubbleDown] < self.elements[largerChild]:
	    #print "swap toBubbleDown:"+str(self.elements[toBubbleDown])+"with child"+str(self.elements[largerChild])	    
	    self.swap(toBubbleDown,largerChild)
            toBubbleDown = largerChild
	    largerChild = self.largerChild(toBubbleDown)
    def largerChild(self,i):
	#no children exist
	if (2*i)+1 >= len(self):
	    return None
	#only one child exists
	elif (2*i)+2 >= len(self):
	    return (2*i)+1
	#find the larger of two children
	elif self.elements[(2*i)+1] > self.elements[(2*i)+2]:
	    return (2*i)+1
	else:
	    return (2*i)+2



largerHalf = MinHeap()
smallerHalf = MaxHeap()
accumMedian = 0

inputFile = open("MedianInput.txt","r")
for line in inputFile.readlines():
    newElement = int(line.rstrip())

    #keep the heapsize equal, and determine the median from the root
    #add in the right heap
    if len(largerHalf) == 0:
	#only largerHalf is checked, this assures sorting the first 2 elements in the right order
	smallerHalf.addElement(newElement) 
    elif newElement > largerHalf.elements[0]:
	largerHalf.addElement(newElement)
    else: 
	smallerHalf.addElement(newElement)

    #balance out the heapsizes again
    if len(largerHalf) > len(smallerHalf):
	smallerHalf.addElement(largerHalf.popRoot())
    elif len(largerHalf) < len(smallerHalf):	 
	largerHalf.addElement(smallerHalf.popRoot())
    else:
	pass

    #find the median 
    #So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,...,xk; 
    #if k is even, then mk is the (k/2)th smallest number among x1,...,xk.
    if len(largerHalf) > len(smallerHalf):
	median = largerHalf.elements[0]
	accumMedian += largerHalf.elements[0]
    elif len(largerHalf) <= len(smallerHalf):
	median = smallerHalf.elements[0]
	accumMedian += smallerHalf.elements[0]
    
    print str(len(smallerHalf)), 
    print "-", 
    if len(smallerHalf)>0:
	print str(smallerHalf.elements[0]),
    print "-", 
    print median,
    print "-", 
    print str(largerHalf.elements[0]),
    print "-", 
    print str(len(largerHalf)),
    print "\n",
print "The summarized median is:"+str(accumMedian)

"""
#test heap functionality, expect ordered numbers from smallest to largest
print "heap from smallest to largest:"
for e in range(len(smallerHalf)):
    print str(smallerHalf.popRoot()),
"""
    
    


