
# task 1

# last character of each element
# sentence is one string
# "-a".append(elem)

uSent = ""

def mario_converter(uSent):
    uSent = input("enter any sentence:")
    temp = uSent.split() # splits the sentence into a list of each word
    uSent ="" # resets the initial variable that you are going to send back

    for i in range(len(temp)): # for looping for the size of the list of words in the sentence
        if not temp[i].endswith("a"): # checking to see if the word doesnt end with an 'a'
            uSent += temp[i] + "-a " # if it doesn't end with an 'a' then you add the word + '-a '
        else:
            uSent += temp[i] + " " #If it does end with an a, just add the word back with a space

    return uSent


print(mario_converter(uSent))


# part 2 task 1

myStr = "hi there, where is the line to Tim Hortons?"

def accent_convert(i, test):
    if isinstance(test, str):
        for elem in test:
            elem.split(" ") # separates sentence by word
            test.find(i) # find the substring user input
        return test.replace(str(i), "1") # creates new string as output

    return test # if not string, return variable

print(accent_convert("i", myStr)) # creates new string with return
assert(isinstance(myStr, str))
print(myStr)



# task 2

# uString = ""

def count_sub(sub):
    uString = input("enter a message:")
    count = 0
    str_len = len(uString)
    x = uString.find(sub, 0, str_len) + 1
    if x > 0:
        count += 1

        while x != 0:
            new_placeholder = uString.find(sub, x, str_len) + 1
            x = new_placeholder
            if x != 0:
                count += 1
        return count


print(count_sub("d"))

"""for elem in uString:
    elem.split(" ")
    uString.find(sub)"""

# task 3


joe = "David,Sprague,65,72,79"


def isStringNumber(strNum):
    try:
        fNum = float(strNum)
        return True
    except ValueError:
        return False

def aveList(lister):
    temp = lister.split(",")
    # temporary variable to hold the split area
    for i in range(len(temp)): # for the range of each element
        if(isStringNumber(temp[i])):
            temp[i] = int(temp[i]) # if the element is a number, force cast out of string into integer

    print(temp)
    return temp


aveList(joe)

