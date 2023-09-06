
import time
import random

# task one

def isStringNumber(strNum):
    try:
        fNum = float(strNum)
        return True
    except:
        return False


def makePositive(uInput):
    if (isStringNumber(uInput)) is True:
        uNum = float(uInput)
        if uNum < 0.0:
            uNum = abs(uNum)
        if float.is_integer(uNum) is True:
            uNum = int(uNum)
            return uNum
        else:
            return uNum
    else:
        return 0

print(makePositive(-9.3))

# task two

def findDayStupid():
    sec70 = time.time()
    days_years = 60 * 60 * 24 * 365
    extra_time = sec70
    counter = 0
    while extra_time > days_years:
        counter += 1
        extra_time = extra_time - days_years
    return counter

print(findDayStupid())


def findDaySmart():
    sec70 = time.time()
    days_hours = 60 * 60 * 24
    days70 = sec70 / days_hours
    return days70

print(findDaySmart())


# task three
import math

def isPrime(uNum):
    if (isStringNumber(uNum)) is True:
        #uNum = int(uNum)
        if isinstance(uNum, float) == True:
            print("please enter an integer:")
            return uNum
        elif uNum < 0:
            print("not a positive number:")
            return uNum
        else:
            uNum = int(uNum)
            for i in range (2, uNum):
                if uNum % i == 0:
                    return False
            return True
    else:
        print("not a number:")
        return uNum

print(isPrime(81))

