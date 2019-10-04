
# --------- #
# The Rules of Rock, Paper, Scissors, Lizard, Spock:
# 1. Rock crushes Scissors,
# 2. Paper covers Rock,
# 3. Scissors cuts paper,
# 4. Lizard eats paper,
# 5. Spock smashes scissors,
# 6. Rock crushes lizard,
# 7. Paper disproves Spock,
# 8. Scissors decapitates lizard,
# 9. Lizard poisons Spock,
# 10. Spock vaporizes rock.

# Invitation to play the game
# Program menu:
# 1. Single Player Game
# 2. Two Player Game
# 3. Bonus Feature
# 4. User Guide (rules of the game, application instructions)
# 5. Quit

# Import random to let the computer make random choices.


import random
import getpass


# Invitation to play the game.
# First ask if the player wants to play
# Then ask if the game will be against the computer or another player
# Fun Facts Trivia game will randomly choose one of the 5 trivia questions for you to answer.
# It will also show your score at the end of the game.

# Invitation to play and game menu.
def invite():
    while True:
        # Rules of the game:
        user_guide = "The Rules of Rock, Paper, Scissors, Lizard, Spock:" \
                     "\n1. Rock crushes Scissors," \
                     "\n2. Paper covers Rock," \
                     "\n3. Scissors cuts paper," \
                     "\n4. Lizard eats paper," \
                     "\n5. Spock smashes scissors," \
                     "\n6. Rock crushes lizard," \
                     "\n7. Paper disproves Spock," \
                     "\n8. Scissors decapitates lizard," \
                     "\n9. Lizard poisons Spock," \
                     "\n10. Spock vaporizes rock." \
                     "\n"
        # Program menu:
        print("\nProgram menu:", "\n1. Single Player Game", "\n2. Two Player Game", "\n3. Bonus Feature",
              "\n4. User Guide", "\n5. Quit")
        menu = int(input("Choose a number from the program menu: "))  # Change input to integer for easier implementing
        if menu == 1:
            print("\nGreat You are playing against me! Let's get started!")
            play ()
        elif menu == 2:
            print("\nOk. Haven fun and good luck to you both!")
            play_2 ()
        elif menu == 3:
            print("\nAs a bonus you can play Five Fun Facts game with me!")
            questions()
        elif menu == 4:
            print(user_guide)
        elif menu == 5:
            print("\nAs you wish. Have a nice day!")
            break


# Single player mode
def play():
    continue_playing = True
    while continue_playing:  # While loop with the True statement which makes it repeat itself until Player quits.
        comp_choice = random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"]) # Randomizing computer choice
        player_choice = input("Choose either Rock, Paper, Scissors, Lizard or Spock. Or type 'Q' to quit: ") # Input for player choice
        print("My choice is:", comp_choice)

        # First check if it's a tie:
        if player_choice.lower() == comp_choice.lower():
            print("It's a tie! Try again!")

        # Then use nested if statements. Check every possible players choice against every possible comp. choice.
        elif player_choice == "rock".lower():
            if comp_choice == "Scissors":
                print("You win! Your Rock crushed my Scissors!", "\n", "This is fun! Let's try again!")
            if comp_choice == "Lizard":
                print("You win! You Rock crushed my Lizard!", "\n", "This is fun! Let's try again!")
            if comp_choice == "Paper":
                print("You lose! Your Rock was covered by my Paper!", "\n", "This is fun! Let's try again!")
            if comp_choice == "Spock":
                print("You lose! Your Rock was vaporized by my Spock!", "\n", "This is fun! Let's try again!")
        elif player_choice == "Paper".lower():
            if comp_choice == "Rock":
                print("You win! Your Paper covered my Rock!", "\n", "This is fun! Let's try again!")
            if comp_choice == "Spock":
                print("You win! Your Paper disproved my Spock!", "\n", "This is fun! Let's try again!")
            if comp_choice == "Scissors":
                print("You lose! Your Paper was cut by my Scissors!", "\n", "This is fun! Let's try again!")
            if comp_choice == "Lizard":
                print("You lose! Your Paper was eaten by my Lizard!", "\n", "This is fun! Let's try again!")
        elif player_choice == "Scissors".lower():
            if comp_choice == "Paper":
                print("You win! Your Scissors cut my Paper!", "\n", "This is fun! Let's try again!")
            if comp_choice == "Lizard":
                print("You win! Your Scissors decapitated my Lizard!", "\n", "This is fun! Let's try again!")
            if comp_choice == "Rock":
                print("You lose! Your Scissors were crushed by my Rock!", "\n", "This is fun! Let's try again!")
            if comp_choice == "Spock":
                print("You lose! Your Scissors were smashed by my Spock!", "\n", "This is fun! Let's try again!")
        elif player_choice == "Lizard".lower():
            if comp_choice == "Paper":
                print("You win! Your Lizard ate my Paper!", "\n", "This is fun! Let's try again!")
            if comp_choice == "Spock":
                print("You win! Your Lizard poisoned my Spock!", "\n", "This is fun! Let's try again!")
            if comp_choice == "Rock":
                print("You lose! Your Lizard was crushed by my Rock!", "\n", "This is fun! Let's try again!")
            if comp_choice == "Scissors":
                print("You lose! Your Lizard was decapitated by my Scissors!", "\n", "This is fun! Let's try again!")
        elif player_choice == "Spock".lower():
            if comp_choice == "Scissors":
                print("You win! Your Spock smashed my Scissors!", "\n", "This is fun! Let's play again!")
            if comp_choice == "Rock":
                print("You win! Your Spock vaporized my Rock!", "\n", "This is fun! Let's try again!")
            if comp_choice == "Paper":
                print("You lose! Your Spock was disproved by my Paper!", "\n", "This is fun! Let's try again!")
            if comp_choice == "Lizard":
                print("You lose! Your Spock was poisoned by my Lizard!", "\n", "This is fun! Let's try again!")

      # If the player wants to quit:
        elif player_choice == "Q".lower():
            print("Ok. It was fun playing with you! Have a nice day!")
            break

       # If the player write something else, which is not part of the game, or with spelling mistakes:
        else:
            print("I didn't understand your choice!")


# Two player mode:
def play_2():
    while True:
        print("Your choices are: Rock, Paper, Scissors, Lizard, Spock. Or type 'Q' to quit!")
        p1_choice = getpass.getpass("Player1 chooses: ")   #getpass works best in terminal, otherwise use input
        p2_choice = getpass.getpass("Player2 chooses: ")

        if p1_choice == p2_choice != "Q".lower():
            print("It's a tie! Try again!")
        elif p1_choice == "Rock".lower():
            if p2_choice == "Paper".lower():
                print("Player1 lost! Paper covered the Rock!")
            if p2_choice == "Scissors".lower():
                print("Player1 won! Rock crushed the Scissors!")
            if p2_choice == "Lizard".lower():
                print("Player1 won! Rock crushed the Lizard!")
            if p2_choice == "Spock".lower():
                print("Player2 won! Spock vaporized the Rock!")
        elif p1_choice == "Paper".lower():
            if p2_choice == "Rock".lower():
                print("Player1 won! Paper covered the Rock!")
            if p2_choice == "Scissors".lower():
                print("Player2 won! Scissors cut the Paper!")
            if p2_choice == "Lizard".lower():
                print("Player2 won! Lizard ate the Paper!")
            if p2_choice == "Spock".lower():
                print("Player1 won! Paper disproved Spock!")
        elif p1_choice == "Scissors".lower():
            if p2_choice == "Rock".lower():
                print("Player2 won! Rock crushed the Scissors!")
            if p2_choice == "Paper".lower():
                print("Player1 won! Scissors cut the Paper!")
            if p2_choice == "Lizard".lower():
                print("Player1 won! Scissors decapitated the Lizard!")
            if p2_choice == "Spock".lower():
                print("Player2 won! Spock smashed the Scissors!")
        elif p1_choice == "Lizard".lower():
            if p2_choice == "Rock".lower():
                print("Player2 won! Rock crushed the Lizard!")
            if p2_choice == "Paper".lower():
                print("Player1 won! Lizard ate the Paper!")
            if p2_choice == "Scissors".lower():
                print("Player2 won! Scissors decapitated the Lizard!")
            if p2_choice == "Spock".lower():
                print("Player1 won! Lizard poisoned Spock!")
        elif p1_choice == "Spock".lower():
            if p2_choice == "Rock".lower():
                print("Player1 won! Spock vaporized the Rock!")
            if p2_choice == "Paper".lower():
                print("Player2 won! Paper disproved Spock!")
            if p2_choice == "Scissors".lower():
                print("Player1 won! Spock smashed the Scissors!")
            if p2_choice == "Lizard".lower():
                print("Player1 won! Lizard posined Spock!")
        elif p1_choice == p2_choice == "Q".lower():
            print("Ok. I hope you had fun! Have a nice day!")
            break
        else:
            print("Oops. I didn't understand that!")

# Bonus feature. Trivia questions
def questions():
    # Explaining the rules to the player
    print("Welcome to the Fun Facts game!"
          "\nYou will be presented with Five Fun Facts questions!"
          "\nAnswer either 'True' or 'False'."
          "\nType 'Q' to quit!"
          "\nType 'M' to return to the Menu!"
          "\nGood luck!"
          "\n")
    # For counting players correct answers out of total amount of questions answered:
    correct_ans = 0
    total_ans = 0

    # For each question - ask for user input, check if the answer is correct,
    # Offer player to quit or return to the main menu.
    # First question.
    q1 = str(input("Frogs can't swallow with their eyes open. True or False? "))
    if q1 == "True".lower():
        print("Correct!")
        correct_ans += 1
        total_ans += 1
    elif q1 == "False".lower():
        print("Wrong. The statement is true!")
        total_ans += 1
    elif q1 == "M".lower():
        invite()
        exit()
    elif q1 == "Q".lower():
        print("Ok. Hope you had fun!")
        print("You had", correct_ans, "correct answers out of", total_ans)
        exit()

    # Second question
    q2 = str(input("Sir Isaac Newton was only 23 when he discovered gravity! True or False? "))
    if q2 == "True".lower():
        print("Correct!")
        correct_ans += 1
        total_ans += 1
    elif q2 == "False".lower():
        print("Wrong. The statement is true!")
        total_ans += 1
    elif q2 == "M".lower():
        invite()
        exit()
    elif q2 == "Q".lower():
        print("Ok. Hope you had fun!")
        print("You had", correct_ans, "correct answers out of", total_ans)
        exit()

    # Third question
    q3 = str(input("25% of people are left handed. True or False? "))
    if q3 == "True".lower():
        print("Wrong. the statement is false!")
        total_ans += 1
    elif q3 == "False".lower():
        print("Correct!")
        correct_ans += 1
        total_ans += 1
    elif q3 == "M".lower():
        invite()
        exit()
    elif q3 == "Q".lower():
        print("Ok. Hope you had fun!")
        print("You had", correct_ans, "correct answers out of", total_ans)
        exit()

    # Fourth question
    q4 = str(input("Virginia Woolf wrote all her books in bed. True or False? "))
    if q4 == "True".lower():
        print("Wrong! The statement is false!")
        total_ans += 1
    elif q4 == "False".lower():
        print("Correct!")
        correct_ans += 1
        total_ans += 1
    elif q4 == "M".lower():
        invite()
        exit()
    elif q4 == "Q".lower():
        print("Ok. Hope you had fun!")
        print("You had", correct_ans, "correct answers out of", total_ans)
        exit()

    # Fifth question
    q5 = str(input("Grasshoppers have white blood. True or False? "))
    if q5 == "True".lower():
        print("Correct!")
        correct_ans += 1
        total_ans += 1
        print("You had", correct_ans, "correct answers out of", total_ans)
        exit()
    elif q5 == "False".lower():
        print("Wrong! The statement is true!")
        total_ans += 1
        print("You had", correct_ans, "correct answers out of", total_ans)
        exit()
    elif q5 == "M".lower():
        invite()
        exit()
    elif q5 == "Q".lower():
        print("Ok. Hope you had fun!")
        print("You had", correct_ans, "correct answers out of", total_ans)
        exit()


if __name__ == "__main__":
    invite()
