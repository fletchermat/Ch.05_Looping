import random
# looping
# for i in range(100,-1,-2):
#     print(i)
# for i in ("HI MARC HERMON"):
#     print(i)
# total = 0
# for i in range(1,101):
#     total += i
# print("The total is",total)

# for i in range(10):
#     print(i)
# print()
# i=0                   same thing
# while i < 10:
#     print(i)
#     i+=1

# i=1
# while i<=2**32:
#     print(i)
#     i*=2

# done = False
# perseverance = 0
# while not done:
#     quit = input("Do you want to quit?")
#     if quit.lower() == "yes":
#         done = True
#     else:
#         perseverance+=1
# print("Goodbye! Your Perseverance level is",perseverance)
#
# for i in range(10):
#     num = random.random()*5+10           random float between 0-15
#     print(num)
done = False
while not done:
    guesses = 0
    num = random.randint(0, 100)
    user = int(input("Im thinking of a number 0 through 100. What is it?"))
    new = False
    while not new:
        if user < num:
            print("Thats too low")
            user = int(input("Guess again?"))
            guesses += 1
        elif user > num:
            print("Thats too high")
            user = int(input("Guess again?"))
            guesses += 1
        else:
            print("It was",num,"you got it in",guesses,"geusses!")
            ask = input("Play again?")
            if ask.lower() == "yes" or ask.lower() == "y":
                new = True
            else:
                new = True
                done = True

print("Goodbye")