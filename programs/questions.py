# INSTRUCTIONS

# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:

# <QUESTION>

# <EXAMPLES>

# <HINT>

# You are allowed access to the internet for this assessment, or you could use the DOCUMENTATION that comes bundled with your Python installation.  You should already be comfortable accessing this documentation, but to summarise:

# Access Python from you CLI

# Type help() or for example help(str)


# <QUESTION 1>

# Define a function that can accept two strings as input and returns the string with maximum length to the console.

# If two strings have the same length, then the function should return both strings separated by a " ".

# In this case, the strings should be returned in the same order in which they were given.

# <EXAMPLES>

# one("hi","hello") → "hello"
# one("three", "two") → "three"
# one("three", "hello") → "three hello"

# <HINT>

# What was the name of the function we have seen to check the length of a container?  Use your CLI to access the Python documentation and get help(len).


def one(input1, input2):
    if len(input1) == len(input2):
        return f"{input1} {input2}"

    else:
        return max(input1, input2, key=len)

        # equivalently we could do
        # if len(input1) > len(input2):
        #   return input1
        # else:
        #   return input2

    # <QUESTION 2>

    # Return the string that is between the first and last appearance of "bert" in the given string

    # Return the empty string "" if there is not 2 occurances of "bert"

    # IGNORE CASE

    # <EXAMPLES>

    # two("bertclivebert") → "clive"
    # two("xxbertfridgebertyy") → "fridge"
    # two("xxBertfridgebERtyy") → "fridge"
    # two("xxbertyy") → ""
    # two("xxbeRTyy") → ""

    # <HINT>

    # What was the name of the function we have seen to seperate a String? How can we make a string all upper or lower case?

    # Use your CLI to access the Python documentation and get help manipulating strings - help(str).


def two(input):
    first_bert = input.casefold().find("bert")
    second_bert = input.casefold().find("bert", first_bert + 4)
    # second argument in str.find allows us to specify where we start looking

    if first_bert != -1 and second_bert != -1:
        # if not found, the result of str.find will be -1
        return input[first_bert + 4 : second_bert]

    else:
        return ""
        # need to return a blank string, can't return nothing!
        # we know this from the examples

    # <QUESTION 3>

    # given a number
    # if this number is divisible by 3 return "fizz"
    # if this number is divisible by 5 return "buzz"
    # if this number is divisible by both 3 and 5 return "fizzbuzz"
    # if this number is not divisible by 3 or 5 return "null"

    # <EXAMPLES>

    # three(3) → "fizz"
    # three(10) → "buzz"
    # three(15) → "fizzbuzz"
    # three(8) → "null"

    # <HINT>

    # No Hints for this question


def three(arg1):
    result = ""

    if arg1 % 3 == 0:
        result += "fizz"
    if arg1 % 5 == 0:
        result += "buzz"

    return result or "null"
    # will return "null" if result is a blank string

    # <QUESTION 4>

    # Given a string seperate the string into the individual numbers present, then add each digit of each number to get a final value for each number

    # String example = "55 72 86"

    # "55" will = the integer 10
    # "72" will = the integer 9
    # "86" will = the integer 14

    # You then need to return the highest value, in the example above this would be 14.

    # <EXAMPLES>

    # four("55 72 86") → 14
    # four("15 72 80 164") → 11
    # four("555 72 86 45 10") → 15

    # <HINT>

    # help(int) for working with numbers and help(str) for working with Strings.


def four(arg1):
    max_value = 0
    for num in map(int, arg1.split()):
        # map(int, ...) will convert a string of numbers back
        # into integers! very handy to know

        value = sum(map(int, str(num)))
        # equivalently could just use a for loop going through str(num), as long
        # as we are converting it into an integer somehow for addition

        if value > max_value:
            max_value = value

    return max_value

    # <QUESTION 5>

    # Given a large string that represents a csv, the structure of each record will be as follows:

    # owner,nameOfFile,encrypted?,fileSize

    # "Bert,helloWorld.py,True,1447,Bert,strings.py,False,1318,Jeff,dice.py,False,1445"

    # For each record, if it is not encrypted, return the names of the owners of the files in a String Array.
    # Do not include duplicate names.
    # If all records are encrypted, return an empty Array.

    # <EXAMPLES>

    # five("Jeff,random.py,False,1445") → ["Jeff"]
    # five("Bert,numberGen.py,True,1447,Bert,integers.py,True,1318,Jeff,floats.py,False,1445") → ["Jeff"]
    # five("Bert,boolean.py,False,1447,Bert,conditions.py,False,1318,Jeff,loops.py,False,1445") → ["Bert","Jeff"]
    # five("Bert,prime.py,True,1447,Bert,ISBN.py,False,1318,Jeff,OOP.py,False,1445") → ["Bert","Jeff"]

    # <HINT>

    # Dont't forget, False is a String, not a Boolean value in the Tests above.

    # help(str) and help(list), you might also need to use a function that can create a list of numbers for you, try help(range).


def five(input):
    result = []
    words = input.split(",")  # get list of words

    for i in range(0, len(words), 4):
        # third argument in range is the step, so we go up by 4 at a time

        name = words[i]  # first argument is the name we want
        encrypted = words[i + 2]  # third argument is whether or not it's encrypted

        if encrypted == "False" and name not in result:
            result.append(name)

    return result

    # <QUESTION 6>

    # There is a well known mnemonic which goes "I before E, except after C", which is used to determine which order "ei" or "ie" should be in a word.

    # Write a function which returns the boolean True if a string follows the mnemonic, and returns the boolean False if not.

    # <EXAMPLES>

    # six("ceiling") → True
    # six("believe") → True
    # six("glacier") → False
    # six("height") → False

    # <HINT>

    # Step through the logic here in order to solve the problem, you may find help(range) helpful.


def six(input):
    return "cei" in input or ("ie" in input and "cie" not in input)
    # not really robust but it passes the tests

    # <QUESTION 7>

    # Write a function which returns the integer number of vowels in a given string.
    # You should ignore case.

    # <EXAMPLES>

    # seven("Hello") → 2
    # seven("hEelLoooO") → 6

    # <HINTS>

    # How do we ignore case in a String? help(str) may offer some insight.


def seven(input):
    vowel_count = 0

    for vowel in "a", "e", "i", "o", "u":

        vowel_count += input.casefold().count(vowel)
        # casefold used to ignore case, as specified in question

    return vowel_count

    # <QUESTION 8>

    # Write a function which takes an input (between 1 and 10 inclusive) and multiplies it by all the numbers before it.
    # eg If the input is 4, the function calculates 4x3x2x1 = 24

    # <EXAMPLES>

    # eight(1) → 1
    # eight(4) → 24
    # eight(8) → 40320

    # <HINT>

    # You may need to create a list of numbers from 0 to i, take a look at help(range).


def eight(input):
    result = 1

    for x in range(1, input + 1):
        # make sure we include the given number, so range should
        # stop at input+1

        result *= x
        # equivalent to result = result * x

    return result

    # <QUESTION 9>

    # Given a string and a char, returns the position in the String where the char first appears.
    # Ensure the positions are numbered correctly, please refer to the examples for guidance.
    # DO NOT ignore case
    # IGNORE whitespace
    # If the char does not occur, return the number -1.

    # <EXAMPLES>

    # nine("This is a Sentence","s") → 4
    # nine("This is a Sentence","S") → 8
    # nine("Fridge for sale","z") → -1

    # <HINT>

    # Take a look at the documentation for Strings, List and range.


def nine(inputString, char):
    inputString = inputString.replace(" ", "")
    actual_index = inputString.find(char)

    if actual_index != -1:
        return actual_index + 1
        # clear from examples it wants it 1-indexed, whereas
        # str.find returns it 0-indexed

    else:
        return -1

    # <QUESTION 10>

    # Given a string, int and a char, return a boolean value if the 'nth'
    # (represented by the int provided) char of the String supplied is the same as the char supplied.
    # The int provided will NOT always be less than than the length of the String.
    # IGNORE case and Whitespace.

    # <EXAMPLES>

    # ten("The",2,'h') → True
    # ten("AAbb",1,'b') → False
    # ten("Hi-There",10,'e') → False

    # <HINT>

    # How do we find the length of a container, take a look at help(len), you will also need to look at help(str) for String manipulation.


def ten(string, int, char):
    string = string.replace(" ", "").casefold()

    if int < len(string):
        return string[int - 1] == char

    else:
        return False
