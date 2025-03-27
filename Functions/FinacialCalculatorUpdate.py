# Evelyn Chennault, Financial Calculator Python

# print satement that welcomes my user and tells what the program does
print("Hello, user. I am a finacial calculator. I will calculate your spendings and savings. Let's begin!\n")

# user inputs
def info(cost, income, type):
    percent= cost/income *100
    print(f"your {type} is ${cost:.2f} rent which is,{percent}%, of your income")

def user(type):
    question = "what is your monthly " + type + "?\n"
    return float(input(question))

income = user("income")
rent = user("rent")
utilities= user("utilities")
groceries= user("groceries")
transportation= user("transportation")
spending= rent+utilities+groceries+transportation
savings = income*0.1

info(rent, income, "rent")
info(utilities, income, "utilites")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(rent, income, "rent")
info(savings, income, "savings")
info(spending,income, "spending")

print("Thank you for trying me out! I hope I helped with your finacial needs.")