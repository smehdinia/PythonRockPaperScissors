    def rockPaperScissors():
        play = True
        while play == True:
            print("Welcome to Rock, Paper, Scissors! Player One, type either\n Rock\n Paper\n Scissors")
            p1choice = input().lower()
            if (p1choice not in ['rock','paper','scissors']):
                print("Try again.")
                return
            print("Player two, input one\n1. Rock\n2. Paper\n3. Scissors")
            p2choice = input().lower()
            if (p2choice not in ['rock','paper','scissors']):
                print("Try again.")
                return
            print("P1: " + p1choice + "\nP2: " + p2choice)
            if (p1choice == p2choice): 
                print("Tie.")
            elif (p1choice == 'rock' and p2choice == 'paper'):
                print("P2 wins")
            elif (p1choice == 'rock' and p2choice == 'scissors'):
                print("P1 wins")
            elif (p1choice == 'paper' and p2choice == 'rock'):
                print("P1 wins")
            elif (p1choice == 'paper' and p2choice == 'scissors'):
                print("P2 wins")
            elif (p1choice == 'scissors' and p2choice == 'paper'):
                print("P1 wins")
            elif (P2choice == 'scissors' and p2choice == 'rock'):
                print("P2 wins")
                
            print("Would you like to play again? Type yes if so. If not, type anything else.")
            answer = input().lower()
            if (answer == 'yes'):
                print("Starting another game.\n")
            else:
                play = False
                return
