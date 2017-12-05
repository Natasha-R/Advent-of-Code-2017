# puzzle input
inputFile = open("C:/Users/Natasha/Desktop/Advent-of-Code-2017/input_5.txt", "r")
origInput = inputFile.readlines()
origInput = [int(line.rstrip()) for line in origInput]
inputFile.close()

# challenge part 1
input = origInput[:]
currentPos = 0
steps = 0
while currentPos < len(input):
    newPos = currentPos + input[currentPos]
    input[currentPos] += 1
    currentPos = newPos
    steps += 1
print("The number of steps it takes to reach the exit is:", steps)

# challenge part 2
input = origInput[:]
currentPos = 0
steps = 0
while currentPos < len(input):
    newPos = currentPos + input[currentPos]
    if input[currentPos] >= 3:
        input[currentPos] -= 1
    else:
        input[currentPos] += 1
    currentPos = newPos
    steps += 1
print("The number of steps it takes to reach the exit is now:", steps)