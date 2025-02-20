# Evelyn Chennault, Financial Calculator Python

print("Hello, user. I am a finacial calculator. I will calculate your spendings and savings. Let's begin!\n")

# user inputs
income = float(input("What is your income?\n"))
rent = float(input("What is your rent?\n"))
utilites = float(input("How much money do you pay for utilites?\n"))
groceries = float(input("How much money do you pay for groceries?\n"))
transportation = float(input("How much money do you pay for transportation?\n"))

print("\n")

savings = income*.1
spendings = (rent+utilites+groceries+transportation)/income


rent_percent = (round(rent/income))*100
utilites_percent = (utilites/income)*100
groceries_percent = (groceries/income)*100
transportation_percent = (transportation/income)*100
savings_percent = (savings/income)*100
spendings_percent = (spendings/income)*100


print(savings, "is 10 percent of your income.")
print(spendings, "which is", spendings_percent, "percent of your income.")
print("Your rent is", rent, "which is", rent_percent, "percent of your income.")
print("Your utilies are", utilites, "which is", utilites_percent, "percent of your income.")
print("Your groceries are", groceries, "which is", groceries_percent, "percent of your income.")
print("Your transportation is", transportation, "which is", transportation_percent, "percent of your income.")
print("Your savings are", savings, "which is", savings_percent, "percent of your income.")
print("Your spendings are", spendings, "which is", spendings_percent, "percent of your income.")