#Evelyn Chennault, Conditionals Notes Python

#1. What puts something inside an "if" statement?
name = input("What is your first name?\n").strip().capitalize()
if name == "Evelyn":
    print("Hello, Evelyn!")
else:
    print(f"Hello, {name}!")


#2. What do "if" statements do?
#Checks the condition, and if it is true, it will perform the given directions.
name = input("What is your first name?\n").strip().capitalize()
if name == "Evelyn":
    print("Hello, Evelyn!")
else: #This happens if the condition is false
    print(f"Hello, {name}!")


#3. What are boolean statements do?
#Part of your conditional that is either true or false
name = input("What is your first name?\n").strip().capitalize()
if name == "Evelyn": #<= This is the boolean statement
    print("Hello, Evelyn!")
else:
    print(f"Hello, {name}!")


#4. What do else statements do?
#Ends the conditonal and gives and outcome to all other inputs.
name = input("What is your first name?\n").strip().capitalize()
if name == "Evelyn":
    print("Hello, Evelyn!")
else: #<= This is the else statement
    print(f"Hello, {name}!")


#5. What kind of statement do you use if you have more than two needed outcomes?
#Computers read from top to bottom, least likely first
num = 2
if num == 0: #<= if always starts the conditional
    print("There are none.")
elif num == 1: #everything inbetween if and else has to bebing with elif
    print("There is one.")
elif num < 4:
    print("There is a couple.")
elif num < 10:
    print("There is a few.")
else: #<= else always ends the conditional
    print("There are many.")


#6. What do each of the different symbols mean in conditionals: <, >, <=, >=, ==, ===, !
#< Less than
#> Greater than
#<= Less than or equal to
#>= Greater than or equal to
#== equal to (one = sets a varible)
#=== *NOT IN PYTHON 
#! Not


#7. What are three logical operators?
#and
if num < 10 and num > 5: #Both boolean statements must be true.
    print("This is a big single digit number.")

#or
if num < 10 or num > 5: #either boolean statements must be true.
    print("This is a big single digit number.")

#not
if not num < 10: #None of the boolean statements can be true.
    print("This is a big single digit number.")

#10. Why do we need logical operators?
#Allows the code to handle more difficult questions, increases complexity.


#11. What do nest conditional statements do?
#
#As many nest conditionals as you want, but recommened no more than 3.

input("How many cookies do I have?\n")
if num < 10:
    if num == 8:
        print("This number is at 8.")
    else:
        if num == 4:
            print ("There are only enough for me...sorry...")
        else:
            print("The number is less than 10.")
else:
    print("ther number is bigger than 10.")
