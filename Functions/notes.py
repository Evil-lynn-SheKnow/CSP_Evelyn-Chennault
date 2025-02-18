# Evelyn Chennault, Function Notes Python

# Functions hold actions to be reused

# camelCase
# snake_case (mostly for python)

# number = int(input("Please tell me a number:\n"))
# def add(numOne, numTwo): # Parameters set the name of the variable (just for the function)
    # return numOne+numTwo

# print(add(number,21)) # Arguements set the value of the variable just for that instance of the function
# addition = add(6,4)
# add(8,12)
# add(64,)
# add(11,10000)
# add(87,3)

def values(type):
    return input(f"Please give me a {type}:\n")

name = values("name")
place = values("place")
verb = values("verb (past tense ONLY)")

print(f"{name} was really fast getting to {place} because they {verb} the whole way there.")