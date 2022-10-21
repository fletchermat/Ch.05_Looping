  #Sign your name:________________
import random
'''
 1. Make the following program work.
'''
# print("This program takes three numbers and returns the sum.")
# total = 0
#
# for i in range(3):
#     user = int(input("Enter a number: "))
#     total += user
# print("The total is:", total)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
# for i in range(2,101,2):
#     print(i)
#


'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
# i = 11
# while i != 0:
#     i -= 1
#     print(i)
# print("Blast off!")
# or
# i = 10
# while i != -1:
#     print(i)
#     i -= 1
# print("Blast Off!")




'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
# num = random.randint(1,10)
# print(num)





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
print("This program asks for seven numbers and then prints the sum.")
total = 0
neg = 0
pos = 0
zero = 0
for i in range(7):
    user = int(input("Enter a number: "))
    total += user
    if user <0:
        neg += 1
    elif user >0:
        pos += 1
    else:
        zero += 1

print("The total is:", total)
if neg > 1 or neg == 0:
    print("There were",neg,"negative numbers")
else:
    print("There was 1 negative number")
if pos > 1 or pos == 0:
    print("There were",pos,"positive numbers")
else:
    print("There was 1 positive number")
if zero > 1 or zero == 0:
    print("There were",zero,"zeros")
else:
    print("There was 1 zero")