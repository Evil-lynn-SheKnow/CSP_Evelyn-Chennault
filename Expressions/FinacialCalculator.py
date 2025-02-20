# Evelyn Chennault, Financial Calculator Python

# print satement that welcomes my user and tells what the program does
print("Hello, user. I am a finacial calculator. I will calculate your spendings and savings. Let's begin!\n")


# ask what their income is (vaible an input)
income = float(input("What is your income?\n"))
# ask what their rent is (vaible an input)
rent = float(input("What is your rent?\n"))
# ask what their utilies is (vaible an input)
utilites = float(input("How much money do you pay for utilites?\n"))
# ask what their groceries is (vaible an input)
groceries = float(input("How much money do you pay for groceries?\n"))
# ask what their transportation is (vaible an input)
transportation = float(input("How much money do you pay for transportation?\n"))
# ask what their savings are (vaible an input)
savings = float(input("How much money do you pay save?\n"))

print("\n")

# calculate savings as 10% of income (income*.1) (varible)
income_percent = (income*.1)
# calculate spending as income-savings-rent-utilites-groceries-transportation
left_over_money = (income-savings-rent-utilites-groceries-transportation)
# calculate what their spendings are (vaible an input)
spendings = (((rent+utilites+groceries+transportation)/income)*100)


# calculate percent income of rent (rent/income*100) (varible)
rent_percent = ((rent/income)*100)
# calculate percent income of utilites (utilites/income*100) (varible)
utilites_percent = ((utilites/income)*100)
# calculate percent income of groceries (groceries/income*100) (varible)
groceries_percent = ((groceries/income)*100)
# calculate percent income of transportation (transportation/income*100) (varible)
transportation_percent = ((transportation/income)*100)
# calculate percent income of spending (savings/income*100) (varible)
savings_percent = ((savings/income)*100)
# calculate percent income of spending (spendings/income*100) (varible)
spendings_percent = ((spendings/income)*100)
# calculate spending as income-savings-rent-utilites-groceries-transportation
left_over_money_percent = ((left_over_money/income)*100)


# ten percent of your income
print(income_percent, "is 10 percent of your income.")
# money left over after all the monthly spending and saving
print(left_over_money, "which is", left_over_money_percent, "percent of your income.")
# your rent is $XX.XX which is XX% of your income. (print)
print("Your rent is", rent, "which is", rent_percent, "percent of your income.")
# your utilities is $XX.XX which is XX% of your income. (print)
print("Your utilies are", utilites, "which is", utilites_percent, "percent of your income.")
# your groceries is $XX.XX which is XX% of your income. (print)
print("Your groceries are", groceries, "which is", groceries_percent, "percent of your income.")
# your transportation is $XX.XX which is XX% of your income. (print)print("Your rent is", rent, "which is", incomePercent, "of your income.")
print("Your transportation is", transportation, "which is", transportation_percent, "percent of your income.")
# your savings is $XX.XX which is XX% of your income. (print)
print("Your savings are", savings, "which is", savings_percent, "percent of your income.")
# your spendings is $XX.XX which is XX% of your income. (print)
print("Your spendings are", spendings, "which is", spendings_percent, "percent of your income.")
# any left over money is $XX.XX which is XX% of your income. (print)
print("You have", left_over_money, "which is", left_over_money_percent, "percent of your income.")

print("\n")

print("Thank you for trying me out! I hope I helped with your finacial needs.")