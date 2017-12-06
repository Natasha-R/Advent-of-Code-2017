# importing puzzle input
inputFile = open("C:/Users/Natasha/Desktop/Advent-of-Code-2017/input_6.txt", "r")
input = [int(i) for i in (inputFile.readlines()[0].rstrip().split("\t"))]
inputFile.close()

# challenge part 1
numberOfCycles = 0
cycles = []

while True:
    highestBlock = input.index(max(input))
    currentIndex = highestBlock
    tempToDist = input[highestBlock]
    input[highestBlock] = 0
    
    for i in range(tempToDist):
        if currentIndex + 1 >= len(input):
            currentIndex = -1
        currentIndex += 1
        input[currentIndex] += 1
        
    numberOfCycles += 1
    tempCycle = "".join(str(i) for i in input)
    if tempCycle in cycles:
        break
    else:
        cycles.append(tempCycle)

print("The number of redistribution cycles needed is:", numberOfCycles)

# challenge part 2
numberOfCycles = 0
cycles = []
cycleFound = False

while True:
    highestBlock = input.index(max(input))
    currentIndex = highestBlock
    tempToDist = input[highestBlock]
    input[highestBlock] = 0
    
    for i in range(tempToDist):
        if currentIndex + 1 >= len(input):
            currentIndex = -1
        currentIndex += 1
        input[currentIndex] += 1
    
    if cycleFound:
        numberOfCycles += 1
        
    tempCycle = "".join(str(i) for i in input)
    if tempCycle in cycles:
        cycles = [tempCycle]
        if cycleFound:
            break
        cycleFound = True
    else:
        cycles.append(tempCycle)

print("The number of cycles in the infinite loop is:", numberOfCycles)