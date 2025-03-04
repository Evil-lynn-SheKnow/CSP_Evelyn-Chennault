#Evelyn Chennault, Old Enough Python

print("Hello! I will determine if you can legally have certain privileges in the USA.")
num = int(input("How old are you?\n"))
print("\n")

#If you can vote
if num >= 5 and num <= 11:
    print("You can not vote, get a learners permit, or drive, but you can go to school.")
elif num >= 12 and num <= 14:
    print("You can not vote or drive, but you can get a learners permit and go to school.")
elif num >= 15 and num <= 17:
    print("You can not vote, but you can get a learners permit, drive and go to school.")
elif num >= 18:
    print("You can vote, get a learners permit, drive, and go to school.")
else: 
    print("You can not vote, get a learners permit, drive, or go to school.")
