#Evelyn Chennault, Loops Notes Python

#1. What is a loop? 
    #Section of code that repeats multiple times.


#2. What are the two types of loops?
    #for loop
nums = [12,3,66,7,3,3,2]

for num in nums:
    print(num)
x = 0

    #while loop
while x < 10:
    print(x)
    x+= 1


#3. What is iteration?
    #Particular instance/time of the loop
    #Iteration is the amount of times you are looping through something


#4. What are lists? 
    #A group of many things that are related
    #A varible that holds multiple values
    #Array


nums = [1,2,3,4,5,6,7,8]
cousins = ["Riely","Brooklyn", "Tyson", "Troy", "Dylan", "Ruby"]
#print(nums) #prints whole list with brackets and coommas, ugly
print(cousins[3])

cousins.pop()
cousins.insert(0, "Anson")
cousins.insert(2, ["person", "person_two", "person_three"])
print(cousins)


#5. How do you make lists in Python? 
    #Use [] brakcets
    #Add in items with correct data types
    #Have to have a comma between each item

    #YOU CAN HAVE A LIST OF LISTS!!!


#6. How do you make for loops in Python? 
    #
for cousin in cousins:
    print(cousin)

for x in range(1,5):
    print(x)


#7. How do you make while loops in Python?
    #
import random
x = 1 #varible keeps count of my iteration
goose = random.randint(1,20)

while x <= 20:
    if x == goose:
        print("Goose!")
        break #tells the loop to stop
    else:
        print("Burb")
    x+= 1

#continue moves on to the next iteration without finishing