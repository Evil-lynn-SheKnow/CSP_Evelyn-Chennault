#Evelyn Chennault, Old Enough Python

print("Hello. I will determine if you can get your driver's license.")
num = int(input("How old are you?\n"))
if num <= 14:
    print("You are in elementary. Get real.")
elif num == 15 or num == 16 or num == 17:
    print("You can start driving! Yay!")
elif num >= 18:
    print("You can drive. If you can't drive or don't have a license, you have a problem.")
else: 
    print("Child. You are a child. The road would be dangerous if you even dared to steer a car.")