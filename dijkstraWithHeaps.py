#Input: directed graph with nonnegative weights, source vertex

#Output: for each vertex the lenght of the shortest path from the source 

#Idea: Use Dijikstra's algorithm using heaps

class Arc():
    def __init__(self,pointsTo = None, weight = None):
	self.pointsTo = pointsTo
	self.weight = weight


class Vertex():
    def __init__(self,idNumber):
	self.nr = idNumber
	self.leavingArcs = [] #list of arcs
	 #shortest length so far, is final as soon as completed is True
	self.shortestLength = float("inf")	
	self.completed = False
	self.positionInHeap = None #alternative: hashtable in heap 
    def addArc(self,arc):
	self.leavingArcs.append(arc)
    

class Graph():
    def __init__(self,n):
	self.vertices =[]
	self.heap=Heap()
	for i in range(1,n+1):
	    self.vertices.append(Vertex(idNumber = i))
    def extractMin(self):
	return self.heap.extractMin()
    def overwrite(self,vertex,newLength):
	vertex.shortestLength = newLength
	if vertex.positionInHeap == None:
	    self.heap.insert(objectToInsert = vertex,key= newLength)
	else:
	    self.heap.updateSmallerKeyAt(vertex.positionInHeap)
    def printyourself(self):
	print "\nGraph:"
	for v in self.vertices:
	    print "\n"+repr(v.nr) +" : "+ repr(v.shortestLength)+" : "+repr(v.completed)
	    print "arcsTo"
	    for a in v.leavingArcs:
		print repr(a.pointsTo.nr),

	print

class Heap(object):
    """
    minimum heap, parents are smaller than their children
    keep vertex.positionInHeap updated to be able to delete elements faster
    """
    class Node(object):
	def __init__(self, objectToStore ,key):
	    self.objectToStore = objectToStore
	    self.key= key
    def __init__(self):
	self.nodes = []
    def parent(self,i):
	if i%2 == 0:
	    return i/2 -1
	else:
	    return i//2
    def smallestChild(self,i):
	return min((2*i)+1,(2*i)+2)
    def swap(self,i,j):
	self.nodes[i], self.nodes[j]= self.nodes[j], self.nodes[i]
	#update vertex.positionInHeap
	self.nodes[i].objectToStore.positionInHeap = i
	self.nodes[j].objectToStore.positionInHeap = j
    def deleteLastElement(self):
	self.nodes[-1].objectToStore.positionInHeap = None
	self.nodes.pop(-1)
    def updateSmallerKeyAt(self, position):
	#how to find the right element ?????
	#bubble-up as needed
	toBubbleUp = position
	while toBubbleUp > 0 and\
	    self.nodes[toBubbleUp].key < self.nodes[self.parent(toBubbleUp)].key:
	    self.swap(toBubbleUp,self.parent(toBubbleUp))
	    toBubbleUp = self.parent(toBubbleUp)
    def printyourself(self):	
	print "\n"
	for a in self.nodes:
	    print repr(a.key) + ":" + repr(a.objectToStore.nr) + "\t",
    def insert(self, objectToInsert, key):
	#add to the buttom
	self.nodes.append(self.Node(objectToInsert,key))
	objectToInsert.positionInHeap = len(self.nodes)-1
	#swap with parents till in correct order; bubble-up
	toBubbleUp = len(self.nodes)-1
	while toBubbleUp > 0 and\
	    self.nodes[toBubbleUp].key < self.nodes[self.parent(toBubbleUp)].key:
	    self.swap(toBubbleUp,self.parent(toBubbleUp))
	    toBubbleUp = self.parent(toBubbleUp)
    def extractMin(self):
	"""
	returns object with minimum key while removing it from the heap, and
	reorders the heap
	"""
	#swap root with element at the buttom
	self.swap(0,-1)
	minObject = self.nodes[-1].objectToStore
	self.deleteLastElement()
	#swap with smallest child till in correct order; bubble-down
	toBubbleDown = 0
	while self.smallestChild(toBubbleDown) <= (len(self.nodes)-1) and\
	    self.nodes[toBubbleDown].key > self.nodes[self.smallestChild(toBubbleDown)].key:
	    self.swap(toBubbleDown, self.smallestChild(toBubbleDown))
	    toBubbleDown = self.smallestChild(toBubbleDown)
	return minObject


def computeShortestDistance(start, end):
	#read input from file and initalize graph
	""" smaller test file
	n=5
	graph = Graph(n)
	targetVertex = graph.vertices[4]
	startingVertex = graph.vertices[0]
	inputfile = open("dijkstraTestInput.txt","r")
	"""

	n=49
	graph = Graph(n)
	targetVertex = graph.vertices[end]
	startingVertex = graph.vertices[start]
	inputfile = open("connect_22_to_26.txt","r")
	"""
	n=200
	graph = Graph(n)
	targetVertex = graph.vertices[end]
	startingVertex = graph.vertices[start]
	inputfile = open("dijkstraInput.txt","r")
	"""
	"""
	n=11
	graph = Graph(n)
	targetVertex = graph.vertices[n-1]
	startingVertex = graph.vertices[0]
	inputfile = open("dijkstraTestInput2.txt","r")
	"""

	lines = inputfile.readlines()
	for line in lines:
	    arcs = line.rstrip().split()
	    newVertex = graph.vertices[int(arcs[0])-1]
	    for arc in arcs[1:]:
		newArc = Arc(	pointsTo = graph.vertices[int(arc.split(",")[0])-1],\
				weight = int(arc.split(",")[1]))
		newVertex.addArc(newArc)
	 
	#dijkstra
	#set put startingVertex into heap
	graph.overwrite(vertex = startingVertex, newLength = 0)
	#till all the nodes are calculated/target node calculated
	while(targetVertex.completed == False):
	    #choose vertix with the smallest distance -> newestCompletedV = heap.extractMin()
	    newestCompletedV = graph.extractMin()
	    #move it to the already completed part of the graph /mark as completed
	    newestCompletedV.completed = True
	    #calculate and update(choosing lowest) new distances connecting  w and any vertices		#not yet completed,

	    #update the arcs where the head doesn't point to a completed vertex
	    for arc in newestCompletedV.leavingArcs:
		if (arc.pointsTo.completed == False):
		    newDistance = newestCompletedV.shortestLength + arc.weight
		    #print newDistance
		    #print arc.pointsTo.shortestLength
		    if newDistance < arc.pointsTo.shortestLength: 
			graph.overwrite(vertex = arc.pointsTo, newLength = newDistance)
		
	print "shortest path to " + repr(graph.vertices[end].nr) + " is " + repr(graph.vertices[end].shortestLength) + repr(graph.vertices[end].completed)


computeShortestDistance(21,25)
#for a in [6,36,58,81,98,114,132,164,187,196]:
#    computeShortestDistance(0,a)
#
#
#
