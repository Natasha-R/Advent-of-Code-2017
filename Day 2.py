# importing puzzle input
inputFile = open("C:/Users/Natasha/Desktop/Advent-of-Code-2017/input_2.txt", "r")
input = inputFile.readlines()
for i in range(len(input)):
    input[i] = input[i].rstrip("\n")
    input[i] = input[i].split("\t")
    input[i] = list(map(int, input[i]))
inputFile.close()

# challenge part 1
sum = 0
for row in input:
    sum += max(row) - min(row)
print("The checksum for the spreadsheet is:", sum)

# challenge part 2
sum = 0
for row in input:
    for i in row:
        for j in row:
            if (i % j == 0) and (i != j):
                sum += i / j
print("The sum of each row's result is:", int(sum))