# importing puzzle input
inputFile = open("C:/Users/Natasha/Desktop/Advent-of-Code-2017/input_4.txt", "r")
input = inputFile.readlines()
newInput = [line.split("\n")[0].split(" ") for line in input]
inputFile.close()

# challenge part 1
numValidLines = 0
for line in newInput:
    lineValid = True
    for word in line:
        if line.count(word) > 1:
            lineValid = False
    if lineValid:
        numValidLines += 1
print("The number of passphrases that are valid is:", numValidLines)

# challenge part 2
numValidLines = 0
for line in newInput:
    lineValid = True
    for word in line:
        if line.count(word) > 1:
            lineValid = False
        for words in line:
            if sorted(word) == sorted(words) and word != words:
                lineValid = False
    if lineValid:
        numValidLines += 1
print("The number of passphrases that are now valid is:", numValidLines)