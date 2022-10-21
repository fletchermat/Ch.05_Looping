'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
import random
done = False
tails = 0
heads = 0
while not done and heads + tails < 50:
    flip = random.randint(0,1)
    if flip == 0:
        print("\033[1;34m Heads")
        heads += 1
    else:
        print("\033[1;31m Tails")
        tails += 1
print("\033[0;0m There were \033[1;34m",heads,"\033[0;0m heads and\033[1;31m ",tails,"\033[0;0m tails")
done = True








