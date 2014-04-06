#Input: array of positive numbers 
#Output:does a combination x+y=t exist?  try for every t in interval [2500,4000]
#   taking care that x and y are "distinct"
#   numbers x,y satisfying x+y=t
#Idea: use hashtable, therefore discarding dublicates

#read numbers and add to hashtable
inputFile = open("HashIntInput.txt","r")
hashtable = {}
for line in inputFile.readlines():
    key = int(line.rstrip())
    #exclude numbers exceding the upper border of t
    if key <= 4000:
	hashtable[key] = True
    
solutionCounter = 0
for t in range(2500,4001):
    for xKey in hashtable:
	lookingForY = t - xKey
	if lookingForY in hashtable and lookingForY != xKey:
	    solutionCounter +=1
	    break

print "number of combinations satisfying x+y=t: "+repr(solutionCounter)
