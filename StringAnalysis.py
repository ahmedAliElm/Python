def numberOfWords(string):

    j = 0
    k = 1
    words = 0

    for i in string:

        if i == ' ' or k == len(string) - 1:

            temp = ''

            while j < k:
                if string[j] != ' ':  # to ignore spaces
                    temp += string[j]
                j += 1

            if temp.isalpha() and len(temp) > 1: # temp has to be all letters and at least two letters long
                words += 1

        k += 1

    print("Number of words:", words)

def numberOfIntegers(string):

    integers = 0
    temp = ''
    j = 0

    for i in string:

        if i != ' ':  # to ignore spaces 
            temp += i  # temp takes the words once it finds space it stops

        if i == ' ' or j == len(string) - 1:

            try:
                int(temp)
                answer = True
            except:
                answer = False

            if answer:
                integers += 1

            temp = ''  # renew temp so as not to have the previous values

        j += 1
    
    print("Number of integers:", integers)

def numberOfPunctuations(string):

    punc = 0
    temp = ''
    x = True
    k = 0

    for i in string:

        if i != ' ':
            temp += i

        if i == ' ' or k == len(string) - 1:

            try:
                float(temp)
                x = True
            except:
                x = False

            if not x:
                for j in temp:
                    if (j == ',' or j == '?' or j == ';' or j == '.' or j == ':' or j == '!'):
                        punc += 1
            
            temp = ''

        k += 1

    print("Number of punctuations:", punc)
    
def numberOfFloats(string):

    floating = 0
    temp = ''
    k = 0

    for i in string:

        if i != ' ':
            temp += i

        if i == ' ' or k == len(string) - 1:

            try:
                float(temp)
                answer = True
            except:
                answer = False

            if answer:
                for j in temp:
                    if j == '.':
                        floating += 1

            temp = ''

        k += 1

    print("Number of floats:", floating)

# Sample:
string = "My name is (your_name) and I am 30 years old. §sqqsvsjhfze'(-) ::;;?56354 23.778 -1  23 -100"
# Enter a string of your choice

numberOfWords(string)
numberOfIntegers(string)
numberOfPunctuations(string)
numberOfFloats(string)