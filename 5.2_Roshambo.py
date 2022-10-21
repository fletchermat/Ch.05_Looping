'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''
import random
done = False
you = 0
computer = 0
ties = 0
print("Welcome to Roshambo!")
print()
print("Type 1 for rock")
print("Type 2 for paper")
print("Type 3 for scissors")
print("Type 4 to quit")
print()
while not done:
    gen = random.randint(1, 3)
    user = input("\033[0;0m Rock, paper, scissors, shoot!")
    # Rocks outcomes
    if user == "1" and gen == 2:
        print("You: Rock")
        print("Computer: Paper")
        print("\033[1;31m You lose")
        print()
        computer += 1
    elif user == "1" and gen == 1:
        print("You: Rock")
        print("Computer: Rock")
        print("\033[1;33m It's a tie")
        print()
        ties += 1
    elif user == "1" and gen == 3:
        print("You: Rock")
        print("Computer: Scissors")
        print("\033[1;32m You win")
        print()
        you += 1
        # Paper outcomes
    elif user == "2" and gen == 3:
        print("You: Paper")
        print("Computer: Scissors")
        print("\033[1;31m You lose")
        print()
        computer += 1
    elif user == "2" and gen == 2:
        print("You: Paper")
        print("Computer: Paper")
        print("\033[1;33m It's a tie")
        print()
        ties += 1
    elif user == "2" and gen == 1:
        print("You: Paper")
        print("Computer: Rock")
        print("\033[1;32m You win")
        print()
        you += 1
        # scissors outcomes
    elif user == "3" and gen == 1:
        print("You: Rock")
        print("Computer: Rock")
        print("\033[1;31m You lose")
        print()
        computer += 1
    elif user == "3" and gen == 3:
        print("You: Rock")
        print("Computer: Scissors")
        print("\033[1;33m It's a tie")
        print()
        ties += 1
    elif user == "3" and gen == 2:
        print("You: Rock")
        print("Computer: Paper")
        print("\033[1;32m You win")
        print()
        you += 1
        # Other outcomes
    elif user == "4":
        done = True
    else:
        print("Type 1 for rock")
        print("Type 2 for paper")
        print("Type 3 for scissors")
        print("Type 4 to quit")
print()
print("\033[0;0m ")
if you == 1:
    print("\033[1;32m You won",you,"time")
else:
    print("\033[1;32m You won", you, "times")
if computer == 1:
    print("\033[1;31m You lost",computer,"time")
else:
    print("\033[1;31m You lost", computer, "times")
if ties == 1:
    print("\033[1;33m You tied",ties,"time")
else:
    print("\033[1;33m You tied",ties,"times")
print("\033[0;0m Goodbye")













