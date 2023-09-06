
# A3 assignment

import math

# determines if a string can be presented as a number
def isStringNumber(strNum):
     try:
        fNum = float(strNum)
        return True
     except ValueError:
        return False


userVal = input("Enter the radius of a circle:")
radius = userVal

#print(type(radius))
#if type(radius) == (float or int):

if isStringNumber(userVal) is True:
    radius = float(userVal)
    radiusSq = radius * radius
#elif isStringNumber(userVal) is True:
  #  radius = int(userVal)
   # radiusSq = radius * radius
    if radius < 0:
     print("please input a positive number!!!!")
    else:
        print("your radius is:", userVal)
        area = math.pi * (radius ** 2)
        print("The area of a circle with radius", userVal, "is:", area,"and its type is", type(area), "\n")
        print("radius squared is", radiusSq, "and its type is", type(radius), "\n")
else:
    print("please enter a number...")

# 12 radius squared is 144.0, area is 452.3893421169302
# 12.0 radius squared is 144.0, area is 452.3893421169302
# because I've cast it as a float


# task 2

bMonth = input("please enter your birth month (P.S. please type January)")

bMonth == "January"
if bMonth != "January":
    print("no its not!! how could you forget your own birth month??")
else:
    bDay = int(input("please enter your birth day"))

if bDay < 1:
    print("that doesn't exist")
elif bDay > 31:
    print("that doesn't exist")
else:
    bYear = int(input("please enter your birth year"))

if bYear < 1922:
    print("EEEEEE A GHOST")
elif bYear > 2021:
    print("how are you using a computer??")
else:
    print("your birth date is:", bMonth, bDay, bYear)


# robot maze is in reflection