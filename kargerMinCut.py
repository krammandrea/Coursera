#Find the minimum cut (number of edges connecting the two disjoint subsets) of the undirected graph

#Input: txt-file where the first column contains all the vertices and the adjoining elements in the same row all the adjacent vertices

#Idea: Karger's contraction algorithm; choose an edge, and collaps it, joining two vertices, eliminate selfloops, do till two vertices left and count the number of edges; repeat n squared times m

import random

def kargersContract():
    #read file into adjecency lists, vertex list pointing to each edge, edge list pointing to two connecting vertices
    vertices =[]

    inputText = open("kargerMinCutInput.txt","r")
    for line in inputText.readlines():
	lineFormatted = line.rstrip().split('\t')
	vertices.append([])
	for vertex in lineFormatted:
	    currentVertex = int(lineFormatted[0]) - 1     #-1 to change range starting with 0
	    if not currentVertex +1 == vertex:		    #remove self-loops
		vertices[currentVertex].append(int(vertex)-1)

    leftOverVertices = range(len(vertices))		

    #do contractions until only two vertices left and count the number of edges
    while len(leftOverVertices) > 2:
    

	#choose a random edge, and contract the two adjoining vertices into 1, replacing one of the vertices with the other in all the lists
	toDiscontinue = leftOverVertices[random.randint(0,len(leftOverVertices)-1)]
	contractTo = vertices[toDiscontinue][random.randint(0,len(vertices[toDiscontinue])-1)]
	    
	#remove self-loops, aka edges with the same vertex at each end
	vertices[toDiscontinue]  = [v for v in vertices[toDiscontinue] if v!=toDiscontinue]
	#print "contractTo:"+repr(contractTo)+"; toDiscontinue: "+repr(toDiscontinue) 	

	leftOverVertices = [v for v in leftOverVertices if v!=toDiscontinue]

	vertices[contractTo] += vertices[toDiscontinue]
	vertices[toDiscontinue] = []

	#rename all the toDiscontinued vertices to contractTo
	#faster alternative: go to the toDiscontinue list and check the list of the vertices named there for toDiscontinued
	vertices = [[(contractTo if vertix==toDiscontinue else vertix) for vertix in lines]for lines in vertices]

	#remove self-loops, aka edges with the same vertex at each end
	vertices[contractTo] = [v for v in vertices[contractTo] if v!=contractTo]

	#print "length: "+repr(len(vertices[contractTo]))+"joinedContracted: " + repr(vertices[contractTo])
    
    return len(vertices[leftOverVertices[0]])	    
 
#repeat algortihm n^2*m times and remember smallest number of edges
repeatTimes = 4000	#TODO reset to n^2*m after debugging
minCut = 50000000 #arbitrary high number
for r in range(repeatTimes):
    someCut = kargersContract()
    if someCut < minCut:
	print someCut
	minCut = someCut
print "minimum Cut: " +repr(minCut)
    
