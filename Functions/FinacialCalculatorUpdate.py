# Evelyn Chennault, Financial Calculator Python

# print satement that welcomes my user and tells what the program does
print("Hello, user. I am a finacial calculator. I will calculate your spendings and savings. Let's begin!\n")

# user inputs
income = float(input("What is your income?\n"))
rent = float(input("How much money do you pay for rent?\n"))
utilites = float(input("How much money do you pay for utilites?\n"))
groceries = float(input("How much money do you pay for groceries?\n"))
transportation = float(input("How much money do you pay for transportation?\n"))
savings = float(income-utilites-groceries-transportation)
spendings = float(utilites+groceries+transportation)


def info(cost, income, type):
    percent1 = rent/income *100
    print(f"Your {type} is {cost:.2} which is {percent1}% of your income.")

def info_two(cost, income, type):
    percent2 = utilites/income *100
    print(f"Your {type} is {cost:.2} which is {percent2}% of your income.")

def info_three(cost, income, type):
    percent3 = groceries/income *100
    print(f"Your {type} is {cost:.2} which is {percent3}% of your income.")

def info_four(cost, income, type):
    percent4 = transportation/income *100
    print(f"Your {type} is {cost:.2} which is {percent4}% of your income.")

def info_five(cost, income, type):
    percent5 = savings/income *100
    print(f"Your {type} is {cost:.2} which is {percent5}% of your income.")

def info_six(cost, income, type):
    percent6 = spendings/income *100
    print(f"Your {type} is {cost:.2} which is {percent6}% of your income.")


income = info("income"), info_two("income"), info_three("income"), info_four("income"), info_five("income"), info_six("income")
rent = info("rent")
utilites = info_two("utilites")
groceries = info_three("groceries")
transportation = info_four("transportation")
savings = info_five("savings")
spendings = info_six("spendings")

print("Thank you for trying me out! I hope I helped with your finacial needs.")