#Find SCCs(strongly connected components, if there is a directed path connecting u to v, as well as v to u)

#Input: directed graph ,txt-file, every row indicates an edge, with the first column being the tail and the second being the head; vertices numbered 1 to 875714

#Idea: Use Kasaraju's two pass algorithm
#1, compute reverse graph with all arcs reversed
#2, run depth-first-search on the reversed graph; discover leaders/"sinks"
#3, run depth-frist-search on the the original graph; starting with the leaders and discover SCCs one by one


#the given assignment has a large recursion depth requiring a larger limit
#also a bigger user limit in the console is required, using about 40000 worked
import sys
sys.setrecursionlimit(100000)

class Vertex ():

    def __init__(self, vertexNumber):
	self.followedBy = []
	self.precededBy = []
	self.nr = vertexNumber
	self.explored = False 
	self.finishingTime = None
    
    def add_precededBy (self, vertex):
	self.precededBy.append(vertex)

    def add_followedBy(self, vertex):
	self.followedBy.append(vertex)

    @classmethod
    def get_finishingTime(cls, vertex):
	return vertex.finishingTime


class Graph():

    def __init__(self):
	self.currFinishingTime = 0
	self.currSccSize = 0
	self.vertices = []

    def append(self,vertex):
	self.vertices.append(vertex)

    def sort_descending_finishingTimes(self):
	self.vertices.sort(key = Vertex.get_finishingTime, reverse = True)

    def reset_explored(self):
	for vertex in self.vertices:
	    vertex.explored = False


def depth_first_search_first_pass(graph, startingVertex):
    
    #mark startingVertex as explored
    startingVertex.explored = True
    
    #go through the graph in reverse order    
    for newVertex in startingVertex.precededBy:
	if newVertex.explored == False:
	    depth_first_search_first_pass(graph, newVertex) 

    startingVertex.finishingTime = graph.currFinishingTime
    graph.currFinishingTime += 1

def depth_first_search_second_pass(graph, startingVertex):
    
    #mark startingVertex as explored
    startingVertex.explored = True
    graph.currSccSize += 1
    
    for newVertex in startingVertex.followedBy:
	if newVertex.explored == False:
	    depth_first_search_second_pass(graph, newVertex) 
    

#smaller test case
#n = 9
#unformattedInput = open("kosarajuSccTestInput.txt","r")


#initialize graph, as a doubly linked list
n = 875714  #number of vertices in kasarajuScc.txt
graph = Graph()
for i in range(n):
    graph.append(Vertex(i))

unformattedInput = open("kosarajuInput.txt","r")
for line in unformattedInput.readlines():
    unformattedLine = line.rstrip().split(' ')
    currentTail = graph.vertices[int(unformattedLine[0])-1]
    currentHead = graph.vertices[int(unformattedLine[1])-1]

    currentTail.add_followedBy(currentHead)
    currentHead.add_precededBy(currentTail)

#run depth first search, using precededBy, and calculate the finishingTime
for vertex in graph.vertices:
    if vertex.explored == False:
	depth_first_search_first_pass(graph, vertex) 

graph.sort_descending_finishingTimes()
graph.reset_explored()

#run depth first search, using followedBy, and remember the number of the just discoverd subsets
result = []
for vertex in graph.vertices:
    if vertex.explored == False:
	depth_first_search_second_pass(graph,vertex);
	#whenever a subset is finished being discovered reset sccSize to zero
	result.append(graph.currSccSize)
	graph.currSccSize = 0

print "number of strongly connected components; 5 largest areas:"
result.sort(reverse = True)
for a in result[0:5]:
    print repr(a) + ",",














