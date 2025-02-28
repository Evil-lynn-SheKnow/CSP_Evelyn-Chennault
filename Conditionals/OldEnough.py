#Evelyn Chennault, Old Enough Python

print("Hello! I will determine if you can legally have certain privileges in the USA.")
print("These privileges are able to\n1. Vote\n2. Get a learner's permit\n3. Drive\n4. Go to school")
num = int(input("How old are you?\n"))
print("\n")

#If you can vote
if num == 4 or num == 5:
    print("1. No")
elif num == 6 or num == 7 or num == 8 or num == 9 or num == 10 or num == 11:
    print("1. No")
elif num == 12 or num == 13 or num == 14:
    print("1. No")
elif num == 15 or num == 16 or num == 17:
    print("1. No")
elif num >= 18:
    print("1. Yes")
else: 
    print("1. You're so cute...wait in a decade and a half, kid")


#If you can get a learner's permit
if num == 4 or num == 5:
    print("2. No")
elif num == 6 or num == 7 or num == 8 or num == 9 or num == 10 or num == 11:
    print("2. No")
elif num == 12 or num == 13 or num == 14:
    print("2. No")
elif num == 15 or num == 16 or num == 17 or num == 18:
    print("2. Yes")
elif num >= 18:
    print("2. Yes")
else: 
    print("2. The road would be dangerous if you even dared to steer a car")


#If you can drive
if num == 4 or num == 5:
    print("3. No")
elif num == 6 or num == 7 or num == 8 or num == 9 or num == 10 or num == 11:
    print("3. No")
elif num == 12 or num == 13 or num == 14:
    print("3. No")
elif num == 15 or num == 16 or num == 17:
    print("3. Yes")
elif num >= 18:
    print("3. Yes")
else: 
    print("3. Stick with HotWheels and the movies--that's safer for everyone")


#If you can go to school
if num == 4 or num == 5:
    print("4. No")
elif num == 6 or num == 7 or num == 8 or num == 9 or num == 10 or num == 11:
    print("4. Yes")
elif num == 12 or num == 13 or num == 14:
    print("4. Yes")
elif num == 15 or num == 16 or num == 17:
    print("4. Yes")
elif num == 18:
    print("4. Yes")
elif num > 18:
    print("4. Yes")
else: 
    print("4. Learn to walk, write, solve math problems, and then we'll talk")
