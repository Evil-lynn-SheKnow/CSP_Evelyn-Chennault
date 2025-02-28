#Evelyn Chennault, Old Enough Python

print("Hello! I will determine if you can legally have certain privileges in the USA.")
print("These privileges are\n1. voting\n2. getting a learner's permit\n3. driving\n4. going to school.")
num = int(input("How old are you?\n"))

print("\n")

#If you can vote
if num == 4 or num == 5:
    print("No votes for you yet.\n")
elif num == 6 or num == 7 or num == 8 or num == 9 or num == 10 or num == 11:
    print("Worry about other things right now. Just be a kid, kid.")
elif num == 12 or num == 13 or num == 14:
    print("You are not mature enough. In a few years, yes, but not now.")
elif num == 15 or num == 16 or num == 17:
    print("So close, and yet, so far...")
elif num >= 18:
    print("You can vote! You better--we need more public opinion.")
else: 
    print("You're so cute...wait in a decade and a half, kid.")


#If you can get a learner's permit
if num == 4 or num == 5:
    print("No vroom-vroom yet.")
elif num == 6 or num == 7 or num == 8 or num == 9 or num == 10 or num == 11:
    print("You are in elementary. Get real.")
elif num == 12 or num == 13 or num == 14:
    print("Get older! That's an order, solider!")
elif num == 15 or num == 16 or num == 17 or num == 18:
    print("You can get your permit now. That might be helpful, just a hunch.")
elif num >= 18:
    print("You have exceeded your permit. Forget supervision! You roll solo.")
else: 
    print("Child. You are a child. The road would be dangerous if you even dared to steer a car.")


#If you can drive
if num == 4 or num == 5:
    print("Leave the driving to the big kids.")
elif num == 6 or num == 7 or num == 8 or num == 9 or num == 10 or num == 11:
    print("Dream on. It'll happen...eventually.")
elif num == 12 or num == 13 or num == 14:
    print("Man. Just out of reach.")
elif num == 15 or num == 16 or num == 17:
    print("You can start driving! Yay! Just watch out for black ice!!!")
elif num >= 18:
    print("You can drive. If you can't drive or don't have a license, you have a problem.")
else: 
    print("Stick with HotWheels and the movies. That's safer for everyone.")


#If you can go to school
if num == 4 or num == 5:
    print("Almost!\n")
elif num == 6 or num == 7 or num == 8 or num == 9 or num == 10 or num == 11:
    print("You can attend a school right now.")
elif num == 12 or num == 13 or num == 14:
    print("Early teens have it easier than you think.")
elif num == 15 or num == 16 or num == 17:
    print("You should be in high school. Welcome to the cursed world of essays and annotated biblographies!")
elif num == 18:
    print("You are almost done with high school--onto college. Achive your drea job!")
elif num > 18:
    print("You should be either in college or working or being a stay-at-home parent.")
else: 
    print("Learn to walk, write, solve math problems, and then we'll talk.")
