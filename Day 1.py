# importing puzzle input
inputFile = open("C:/Users/Natasha/Desktop/Advent-of-Code-2017/input_1.txt", "r")
input = int(inputFile.read())
input = list(map(int, str(input)))
inputFile.close()

# challenge part 1
sum = 0
for i in range(len(input) - 1):
    if (input[i] == input[i + 1]):
        sum += input[i]
if (input[0] == input[len(input) - 1]):
    sum += input[0]
print("The solution to the captcha is:", sum)

# challenge part 2
sum = 0
halfway = len(input)//2
for i in range(len(input)):
    if (i + halfway) > (len(input) - 1):
        if (input[i] == input[i + halfway - len(input)]):
            sum += input[i]
    else:
        if (input[i] == input[i + halfway]):
            sum += input[i]
print("The solution to the new captcha is:", sum)