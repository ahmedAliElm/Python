def rockPaperScissors():

    i = 0

    while i < 3: # to repeat 3 times (optional)

        player1 = input("Player 1 : Choose rock/paper/scissors : ")
        player2 = input("Player 2 : Choose rock/paper/scissors : ")

        if player1 == "rock":

            if player2 == "scissors":
                print("Player 1 wins!")

            elif player2 == "paper":
                print("Player 2 wins!")

            elif player2 == "rock":
                print("It's a tie!")

        elif player1 == "scissors":

            if player2 == "paper":
                print("Player 1 wins!")

            elif player2 == "rock":
                print("Player 2 wins!")

            elif player2 == "scissors":
                print("It's a tie!")

        elif player1 == "paper":

            if player2 == "rock":
                print("Player 1 wins!")

            elif player2 == "scissors":
                print("Player 2 wins!")

            elif player2 == "paper":
                print("It's a tie!")

        i += 1 

rockPaperScissors()

