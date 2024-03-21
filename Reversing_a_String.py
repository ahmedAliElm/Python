def reverse(string):

    i = 0
    k = len(string) - 1
    temp = ''

    while i < len(string):
        temp += string[k]
        k -= 1
        i += 1

    return temp

myString = "I love Python"
print(inversion(myString))

