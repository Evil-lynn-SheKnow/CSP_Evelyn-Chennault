# Evelyn Chennault, Financial Calculator Python

# print satement that welcomes my user and tells what the program does
print("Hello, user. I am a finacial calculator. I will calculate your spendings and savings. Let's begin!\n")

# user inputs
income = float(input("What is your income?\n"))

def info(type):
    return input(f"How much do you have to pay for {type}:\n")

rent = info("rent")
utilites = info("utilites")
groceries = info("groceries")
transportation = info("transportation")

rent_per = round(rent/income*100)
utilites_per = utilites/income*100
groceries_per = groceries/income*100
transport_per = transportation/income*100
savings = income*.1
spendings = income-rent-utilites-groceries-transportation-savings

print(f"Your is ${income}.")
print(f"You spend ${rent} for your rent, which is {rent_per}% of your income.")
print(f"You spend ${utilites} for your utilites, which is {utilites_per}% of your income.")
print(f"You spend ${groceries} for your groceries, which is {groceries_per}% of your income.")
print(f"You spend ${transportation} for transportation, which is {transport_per}% of your income.")
print(f"You spend ${spendings} for all purposes,.")
print(f"${savings} is 10% of your income.")

print("Thank you for trying me out! I hope I helped with your finacial needs.")