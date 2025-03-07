#Evelyn Chennault, FizzBuzz Python

while x:
    x = int(input("Type in a number between 1 and 100:\n"))
    if x % 3 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else: 
        print(x)
    x += 1