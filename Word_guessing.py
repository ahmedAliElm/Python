word = ""  # enter a word of your choice
x = False  # set x to False for the while loop

while not x:  # while x == False

    guess = input("Enter your guess: ")

    if guess == word:
        x = not x  # x = True
        print("Correct guess!")
        break

    print("Wrong guess, try again")

    