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

    if len(str(input1)) > len(str(input2)) :
       return (input1)

    elif len(str(input1)) > len(str(input2)):
       return (input2)

    else:
       return (input1) (" ") (input2)

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
    return input(word.lower.split('bert'))

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
    if arg1 % 3 == 0 and arg1 % 5 == 0:
        result1 = "FizzBuzz"
        return(arg1, result1)
    elif arg1 % 3 == 0:
        result2 = "Fizz"
        return(arg1, result2)
    elif arg1 % 5 == 0:
        result3 = "Buzz"
        return(arg1, result3)

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
    four = 0
    for x in arg1:
        if x.isdigit() == True:
            z = int(x)
            four = four + z

    return four

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
    pass


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
    def check(input):
      if "cie" in input:
        return False
      elif "cei" in input:
        return True
      elif "ei" in input:
        return False
      elif "ie" in input:
        return True
      else:
        return True

    # <QUESTION 7>

    # Write a function which returns the integer number of vowels in a given string. 
    # You should ignore case.

    # <EXAMPLES>

    # seven("Hello") → 2
    # seven("hEelLoooO") → 6

    # <HINTS>

    # How do we ignore case in a String? help(str) may offer some insight.


def vowel():
    return input.lower() in ['a', 'e', 'i', 'o', 'u']

def seven(input):
    count = 0
    for i in range(len(str)):
        if vowel(str[i]):
            count += 1
    return count
 
    


    # <QUESTION 8>

    # Write a function which takes an input (between 1 and 10 inclusive) and multiplies it by all the numbers before it.
    # eg If the input is 4, the function calculates 4x3x2x1 = 24 

    # <EXAMPLES>

    # eight(1) → 1
    # eight(4) → 24
    # eight(8) → 40320

    # <HINT>

def eight(input)
    for range (1, 10)
    (int(input))
    ################## I've no time to finish this

    # You may need to create a list of numbers from 0 to i, take a look at help(range).

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
    pass


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
    pass
