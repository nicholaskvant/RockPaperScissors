import random
import time

def rockpaperscissors():
    rpc = ['Rock', 'Paper', 'Scissors']

    randomArray = random.randint(0, len(rpc))
    randomChoice = rpc[randomArray - 1]

    print("*-----------------------------*")
    print("Welcome to rock paper scissors!")

    time.sleep(0.5)

    guesses = 0

    inp = input("Rock Paper Scissors: ")

    while True:
        if inp == randomChoice:
            print("Tie!")
            print(f"Opponent chooses {inp}")
            randomArray = random.randint(0, len(rpc))
            randomChoice = rpc[randomArray - 1]
            inp = input("Rock Paper Scissors: ")
            playAgain = input("Play again? (Yes/No): ")

            if playAgain == "Yes":
                rockpaperscissors()
            
            if playAgain == "No":
                break

        elif inp == "Rock" and randomChoice == "Paper":
            print("You lose!")
            print(f"Opponent chooses Paper")
            playAgain = input("Play again? (Yes/No): ")

            if playAgain == "Yes":
                rockpaperscissors()
            
            if playAgain == "No":
                break

        elif inp == "Rock" and randomChoice == "Scissors":
            print("You win!")
            print(f"Opponent chooses Scissors")
            playAgain = input("Play again? (Yes/No): ")

            if playAgain == "Yes":
                rockpaperscissors()
            
            if playAgain == "No":
                break

        elif inp == "Paper" and randomChoice == "Rock":
            print("You win!")
            print(f"Opponent chooses Rock")
            playAgain = input("Play again? (Yes/No): ")

            if playAgain == "Yes":
                rockpaperscissors()
            
            if playAgain == "No":
                break

        elif inp == "Paper" and randomChoice == "Scissors":
            print("You lose!")
            print(f"Opponent chooses Scissors")
            playAgain = input("Play again? (Yes/No): ")

            if playAgain == "Yes":
                rockpaperscissors()
            
            if playAgain == "No":
                break

        elif inp == "Scissors" and randomChoice == "Rock":
            print("You lose!")
            print("Opponent chooses Rock")
            playAgain = input("Play again? (Yes/No): ")

            if playAgain == "Yes":
                rockpaperscissors()
            
            if playAgain == "No":
                break  

        elif inp == "Scissors" and randomChoice == "Paper":
            print("You win!")
            print(f"Opponent chooses Paper")
            playAgain = input("Play again? (Yes/No): ")

            if playAgain == "Yes":
                rockpaperscissors()
            
            if playAgain == "No":
                break

        else:
            print("Invalid input")
            playAgain = input("Play again? (Yes/No): ")

            if playAgain == "Yes":
                rockpaperscissors()
            
            if playAgain == "No":
                break

rockpaperscissors()