'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
print()
print("\033[1;38m|You were exploring africa and are now traveling back to europe.")
print("|An angry african tribe is chasing you. You are trying to cross ")
print("|the Sahara desert. You have your camel, but you only have so")
print("|much water.")
print()
storm = 0
back = 0
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_distance = -20
canteen = 4
success = 6   # for trap
win = 0
again = "n"       # for play again
done = False
while not done:

    if thirst >= 6:  # Death block
        print("\033[1;31m You Died of thirst.")
        done = True
        break
    elif natives_distance >= miles_traveled:
        print("\033[1;31m You died, the natives caught up with you.")
        done = True
        break
    elif camel_tiredness >= 8:
        print("\033[1;31m Your camel died of exhaustion, you are doomed to die by the natives.")
        done = True
        break
    elif miles_traveled >= 200 and again.lower() != "y":
        print()
        print("\033[1;34m You made it out of the desert!")
        win = 1
        done = True
        break
    if thirst == 4 or thirst == 5:
        print("\033[1;33m You are thirsty.")
    if camel_tiredness == 5 or camel_tiredness == 6 or camel_tiredness == 7:
        print("\033[1;33m Your camel is tired")

    if abs(miles_traveled-natives_distance) <=12 and done == False:
        print("\033[1;33m The natives are close")
    miles_went=0
    print()
    print("\033[0;0mA. Drink from your canteen")
    print("B. Ahead moderate speed")
    print("C. Full speed ahead")
    print("D. Stop for the night")
    print("E. Status check")
    print("F. Set a trap")
    print("Q. Quit")
    print()
    answer = input("Your choice? ")
    if answer.lower() == "q":
        done = True
        print()
    elif answer.lower() == "a":  # drink from canteen
        print()
        if canteen != 0:
            canteen -= 1
            thirst = 0
            print("\033[1;32m You drank from your canteen and fully replenished your thirst.")
            if canteen == 3:
                print("\033[1;32m Your canteen is still mostly filled.")
            elif canteen == 2:
                print("\033[1;33m Your canteen is half empty.")
            elif canteen ==1:
                print("\033[1;33m Your canteen is almost empty.")
            else:
                print("\033[1;33m your canteen is empty.")
        else:
            print("\033[1;33m Your canteen is empty, you cannot drink.")
    elif answer.lower() == "e":      # Status check
        print()
        print("\033[1;37m Distance traveled:",miles_traveled)
        if canteen == 4:
            print(" Your canteen is full.")
        elif canteen == 3:
            print(" Your canteen is still mostly filled.")
        elif canteen == 2:
            print(" Your canteen is half empty.")
        elif canteen == 1:
            print(" Your canteen is almost empty.")
        else:
            print(" Your canteen is empty.")
        if abs(miles_traveled-natives_distance) == 1:
            print(" The natives are 1 mile behind you")
        else:
            print(" The natives are",abs(miles_traveled-natives_distance),"miles behind you")######
    elif answer.lower() == "d":    # Stop for the night
        print()
        if success == 2:
            print("\033[1;32m The natives were set back by your trap")
            natives_distance -= random.randint(5, 40)
            success = 6
        elif success == 1:
            print("\033[1;33m The natives avoided your trap")
            success = 6
        camel_tiredness = 0
        natives_distance += random.randint(7,15)
        thirst +=1
        print("\033[1;32m Your camel is well rested.")

    elif answer.lower() == "c":     # full speed ahead
        print()
        if abs(miles_traveled-natives_distance) > 20 and done == False or storm == 4: #Sandstorm
            storm = random.randint(1,5)
            if storm == 4:
                back = random.randint(5, 12)
                print("\033[1;33m A sandstorm set you back",back,"miles")
                miles_went -= back
                storm = 2
        natives_distance += random.randint(9,16)
        miles_went += random.randint(10,23)
        miles_traveled += miles_went
        thirst += 1
        camel_tiredness += random.randint(1,3)
        if miles_went !=1:
            print("\033[1;32m You traveled",miles_went,"miles.")
        else:
            print("\033[1;32m You traveled 1 mile")
        if success == 2:           # trap result
            print("\033[1;32m The natives were set back by your trap")
            natives_distance -= random.randint(5, 40)
            success = 6
        elif success == 1:
            print("\033[1;33m The natives avoided your trap")
            success = 6
        luck = random.randint(1,20)         # oasis
        if luck == 4 and done == False:
            print("\033[1;32m You found an oasis!")
            print(" Your canteen has been filled.")
            print(" Your thirst is gone.")
            print(" Your camel is well rested.")
            thirst = 0
            camel_tiredness = 0
            canteen = 4

    elif answer.lower() == "b":     # moderate speed ahead
        print()
        if abs(miles_traveled-natives_distance) > 20 and done == False or storm ==4: #Sandstorm
            storm = random.randint(1,5)
            if storm == 4:
                back = 5
                print("\033[1;33m A sandstorm set you back",back,"miles")
                miles_went -= back
                storm = 2
        natives_distance += random.randint(7,15)
        miles_went += random.randint(5,13)
        miles_traveled += miles_went
        thirst += 1
        camel_tiredness += 1
        if miles_went != 1:
            print("\033[1;32m You traveled", miles_went, "miles.")
        else:
            print("\033[1;32m You traveled 1 mile")
        if success == 2:  # trap result
            print("\033[1;32m The natives were set back by your trap")
            natives_distance -= random.randint(5, 40)
            success = 6
        elif success == 1:
            print("\033[1;33m The natives avoided your trap")
            success = 6
        luck = random.randint(1,20)         # oasis
        if luck == 4 and done == False:
            print("\033[1;32m You found an oasis!")
            print(" Your canteen has been filled.")
            print(" Your thirst is gone.")
            print(" Your camel is well rested.")
            thirst = 0
            camel_tiredness = 0
            canteen = 4

    elif answer.lower() == "f":    # set a trap
        print()
        thirst += 1
        if camel_tiredness > 0:
            camel_tiredness -= random.randint(0,1)
        success = random.randint(1,2)
        natives_distance += random.randint(7, 15)
        if natives_distance >= miles_traveled:
            print("\033[1;31m You died, the natives ambushed you as you set up your trap")
            done = True
            break
        else:
            print("\033[1;32m You set a trap.")
    elif answer == "CHEAT":
        natives_distance += random.randint(180,200)
        miles_went = random.randint(200,220)
        miles_traveled += miles_went
        thirst += 1
        camel_tiredness += 1
        print("\033[1;32m You traveled", miles_went, "miles... cheater.")
        if success == 2:  # trap result
            print("\033[1;32m The natives were set back by your trap")
            natives_distance -= random.randint(5, 40)
            success = 6
        elif success == 1:
            print("\033[1;33m The natives avoided your trap")
            success = 6
        luck = random.randint(1, 20)  # oasis
        if luck == 4 and done == False:
            print("\033[1;32m You found an oasis!")
            print(" Your canteen has been filled.")
            print(" Your thirst is gone.")
            print(" Your camel is well rested.")
            thirst = 0
            camel_tiredness = 0
            canteen = 4
    elif answer == "PAIN":
        storm = 4
        natives_distance += random.randint(7,10)
        print()
        print("\033[1;35m You hear thunder in the distance")


if win == 1:
    print()
    again = input(" Continue? y/n: ")
    print()
    if again.lower() == "y":
        done = False
        while not done:

            if thirst >= 6:  # Death block
                print("\033[1;31m You Died of thirst.")
                done = True
                break
            elif natives_distance >= miles_traveled:
                print("\033[1;31m You died, the natives caught up with you.")
                done = True
                break
            elif camel_tiredness >= 8:
                print("\033[1;31m Your camel died of exhaustion, you are doomed to die by the natives.")
                done = True
                break
            elif miles_traveled >= 200 and again.lower() != "y":
                print()
                print("\033[1;34m You made it out of the desert!")
                win = 1
                done = True
                break
            if thirst == 4 or thirst == 5:
                print("\033[1;33m You are thirsty.")
            if camel_tiredness == 5 or camel_tiredness == 6 or camel_tiredness == 7:
                print("\033[1;33m Your camel is tired")

            if abs(miles_traveled-natives_distance) <=12 and done == False:
                print("\033[1;33m The natives are close")
            miles_went=0
            print()
            print("\033[0;0mA. Drink from your canteen")
            print("B. Ahead moderate speed")
            print("C. Full speed ahead")
            print("D. Stop for the night")
            print("E. Status check")
            print("F. Set a trap")
            print("Q. Quit")
            print()
            answer = input("Your choice? ")
            if answer.lower() == "q":
                done = True
            elif answer.lower() == "a":  # drink from canteen
                print()
                if canteen != 0:
                    canteen -= 1
                    thirst = 0
                    print("\033[1;32m You drank from your canteen and fully replenished your thirst.")
                    if canteen == 3:
                        print("\033[1;32m Your canteen is still mostly filled.")
                    elif canteen == 2:
                        print("\033[1;33m Your canteen is half empty.")
                    elif canteen ==1:
                        print("\033[1;33m Your canteen is almost empty.")
                    else:
                        print("\033[1;33m your canteen is empty.")
                else:
                    print("\033[1;33m Your canteen is empty, you cannot drink.")
            elif answer.lower() == "e":      # Status check
                print()
                print("\033[1;37m Distance traveled:",miles_traveled)
                if canteen == 4:
                    print(" Your canteen is full.")
                elif canteen == 3:
                    print(" Your canteen is still mostly filled.")
                elif canteen == 2:
                    print(" Your canteen is half empty.")
                elif canteen == 1:
                    print(" Your canteen is almost empty.")
                else:
                    print(" Your canteen is empty.")
                if abs(miles_traveled-natives_distance) == 1:
                    print(" The natives are 1 mile behind you")
                else:
                    print(" The natives are",abs(miles_traveled-natives_distance),"miles behind you")######
            elif answer.lower() == "d":    # Stop for the night
                print()
                if success == 2:
                    print("\033[1;32m The natives were set back by your trap")
                    natives_distance -= random.randint(5, 40)
                    success = 6
                elif success == 1:
                    print("\033[1;33m The natives avoided your trap")
                    success = 6
                camel_tiredness = 0
                natives_distance += random.randint(7,15)
                thirst +=1
                print("\033[1;32m Your camel is well rested.")
            elif answer.lower() == "c":     # full speed ahead
                print()
                if abs(miles_traveled - natives_distance) > 20 and done == False:  # Sandstorm
                    storm = random.randint(1, 4)
                    if storm == 4:
                        back = random.randint(5, 12)
                        print("\033[1;33m A sandstorm set you back", back, "miles")
                        miles_went -= back
                        storm = 2
                natives_distance += random.randint(8,15)
                miles_went += random.randint(9,23)
                miles_traveled += miles_went
                thirst += 1
                camel_tiredness += random.randint(1,3)
                if miles_went > 1 or miles_went == 0:
                    print("\033[1;32m You traveled", miles_went, "miles.")
                elif miles_went < 0:
                    print("\033[1;33m You were set back", abs(miles_went), "miles")
                else:
                    print("\033[1;32m You traveled 1 mile")
                if success == 2:           # trap result
                    print("\033[1;32m The natives were set back by your trap")
                    natives_distance -= random.randint(5, 40)
                    success = 6
                elif success == 1:
                    print("\033[1;33m The natives avoided your trap")
                    success = 6
                luck = random.randint(1,20)         # oasis
                if luck == 4 and done == False:
                    print("\033[1;32m You found an oasis!")
                    print(" Your canteen has been filled.")
                    print(" Your thirst is gone.")
                    print(" Your camel is well rested.")
                    thirst = 0
                    camel_tiredness = 0
                    canteen = 4
            elif answer.lower() == "b":     # moderate speed ahead
                print()
                if abs(miles_traveled - natives_distance) > 20 and done == False:  # Sandstorm
                    storm = random.randint(1, 5)
                    if storm == 4:
                        back = random.randint(5,12)
                        print("\033[1;33m A sandstorm set you back", back, "miles")
                        miles_went -= back
                        storm = 2
                natives_distance += random.randint(7,15)
                miles_went += random.randint(5,13)
                miles_traveled += miles_went
                thirst += 1
                camel_tiredness += 1
                if miles_went > 1 or miles_went == 0:
                    print("\033[1;32m You traveled", miles_went, "miles.")
                elif miles_went <0:
                    print("\033[1;33m You were set back",abs(miles_went),"miles")
                else:
                    print("\033[1;32m You traveled 1 mile")
                if success == 2:  # trap result
                    print("\033[1;32m The natives were set back by your trap")
                    natives_distance -= random.randint(5, 40)
                    success = 6
                elif success == 1:
                    print("\033[1;33m The natives avoided your trap")
                    success = 6
                luck = random.randint(1,20)         # oasis
                if luck == 4 and done == False:
                    print("\033[1;32m You found an oasis!")
                    print(" Your canteen has been filled.")
                    print(" Your thirst is gone.")
                    print(" Your camel is well rested.")
                    thirst = 0
                    camel_tiredness = 0
                    canteen = 4
            elif answer.lower() == "f":    # set a trap
                print()
                thirst += 1
                if camel_tiredness > 0:
                    camel_tiredness -= random.randint(0,1)
                success = random.randint(1,2)
                natives_distance += random.randint(7, 15)
                if natives_distance >= miles_traveled:
                    print("\033[1;31m You died, the natives ambushed you as you set up your trap")
                    done = True
                    break
                else:
                    print("\033[1;32m You set a trap.")
            elif answer.upper() == "DEAL":
                print()
                thirst -= 2
                natives_distance += random.randint(7,14)
                print("\033[1;35m You sacrifice your blood for water")
                print("\033[1;32m You feel refreshed")
                print("\033[1;33m You shiver")
            elif answer.upper() == "PAIN":
                natives_distance += random.randint(7,14)
                print()
                print("\033[1;35m You hear thunder in the distance")
                print("\033[1;33m You shiver")
            elif answer.lower() == "eyes":
                print()
                natives_distance += random.randint(7, 14)
                print("\033[1;35m You see something shimmer in the distance")
                print("\033[1;32m You found an oasis!")
                print(" Your canteen has been filled")
                print(" Your thirst is gone")
                print(" Your camel is well rested")
                print("\033[1;33m You shiver")
                thirst = 0
                camel_tiredness = 0
                canteen = 4
print("\033[1;34m You went a total of",miles_traveled,"miles.")


