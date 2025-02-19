# Evelyn Chennault, Financial Calculator Python

# print satement that welcomes my user and tells what the program does
print("Hello, user. I am a finacial calculator. I will calculate your spendings and savings. Let's begin!")

# ask what their income is (vaible an input)
income = float(input("What is your income? \n"))
# ask what their rent is (vaible an input)
rent = float(input("What is your rent? \n"))
# ask what their utilies is (vaible an input)
utilites = float(input("How much money do you pay for utilites? \n"))
# ask what their groceries is (vaible an input)
groceries = float(input("How much money do you pay for groceries? \n"))
# ask what their transportation is (vaible an input)
transportation = float(input("How much money do you pay for transportation? \n"))
# ask what their spendings are (vaible an input)
spendings = float(input("How much money do you pay for everything? \n"))
# ask what their savings are (vaible an input)
savings = float(input("How much money do you pay save? \n"))

# calculate savings as 10% of income (income*.1) (varible)
incomePercent = (income*.1)
# calculate spending as income-savings-rent-utilites-groceries-transportation
leftOverMoney = (income-savings-rent-utilites-groceries-transportation)

# calculate percent income of rent (rent/income*100) (varible)
rentPercent = ((rent/income)*100)
# calculate percent income of utilites (utilites/income*100) (varible)
utilitesPercent = ((utilites/income)*100)
# calculate percent income of groceries (groceries/income*100) (varible)
groceriesPercent = ((groceries/income)*100)
# calculate percent income of transportation (transportation/income*100) (varible)
transportationPercent = ((transportation/income)*100)
# calculate percent income of spending (savings/income*100) (varible)
savingsPercent = ((savings/income)*100)
# calculate percent income of spending (spendings/income*100) (varible)
spendingsPercent = ((spendings/income)*100)

# ten percent of your income
print(incomePercent, "is 10 percent of your income.")
# money left over after all the monthly spending and saving
print(leftOverMoney, "is 10 percent f your income.")
# your rent is $XX.XX which is XX% of your income. (print)
print("Your rent is", rent, "which is", rentPercent, "percent of your income.")
# your utilities is $XX.XX which is XX% of your income. (print)
print("Your utilies are", utilites, "which is", utilitesPercent, "percent of your income.")
# your groceries is $XX.XX which is XX% of your income. (print)
print("Your groceries are", groceries, "which is", groceriesPercent, "percent of your income.")
# your transportation is $XX.XX which is XX% of your income. (print)print("Your rent is", rent, "which is", incomePercent, "of your income.")
print("Your transportation is", transportation, "which is", transportationPercent, "percent of your income.")
# your savings is $XX.XX which is XX% of your income. (print)
print("Your savings are", savings, "which is", savingsPercent, "percent of your income.")
# your spendings is $XX.XX which is XX% of your income. (print)
print("Your spendings are", spendings, "which is", spendingsPercent, "percent of your income.")

print("Thank you for trying me out! I hope I helped with your finacial needs.")