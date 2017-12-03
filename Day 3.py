# the right hand corner of the spiral is a sequence of odd numbers squared
rightCornerList = []
i = 1
while (i**2 < 363700):
    rightCornerList.append(i**2)
    i += 2

# the index position of a number relates to which spiral it's on
# taking 1 to be co-ordinate (0, 0), the spiral number hence also relates to the co-ordinate
print("(" + str(-(len(rightCornerList)-2)) + ", " + str(-(len(rightCornerList)-2)) + ")" +
      " position is number " + str(rightCornerList[len(rightCornerList)-2]))
print("(" + str(-(len(rightCornerList)-1)) + ", " + str(-(len(rightCornerList)-1)) + ")" +
      " position is number " + str(rightCornerList[len(rightCornerList)-1]))

# result:
# (-300, -300) position is number 361201
# (-301, -301) position is number 363609

# (363609 - 361201) / 4 = 602, so the length of the sides of the 300th spiral is 602
# as 361201 is in the right hand corner, and 361201 + 602 = 361503,
# then 361527 must be on the right hand vertical side of the spiral: 361527 - 361201 = 326
# hence 361527 must be at co-ordinate: (-300, 26)

# calculating the manhattan distance:
print("The puzzle answer is: ", abs(0--300) + abs(0-26))
