# Words that start with ab and end with cd

def abcd(myString):

    temp = ''
    j = 0

    for i in myString:

        if i != ' ':  # while there is no space meaning that it's one word
            temp += i
        
        if i == ' ' or j == len(myString) - 1: # checks for space or the string is one word

            if temp[0] == 'a' and temp[1] == 'b' and temp[-1] == 'd' and temp[-2] == 'c':
                print(temp)

            temp = ''

        j += 1
         
string = "abaacd khkjhmgh ablmfdikfghmlcd abcd ^sdbùmd abcdiml"

abcd(string)