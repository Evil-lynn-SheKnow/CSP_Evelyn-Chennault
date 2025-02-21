# Evelyn Chennault, Financial Calculator Python

# print satement that welcomes my user and tells what the program does
print("Hello, user. I am a finacial calculator. I will calculate your spendings and savings. Let's begin!\n")


# user inputs
income = float(input("What is your income?\n"))
rent = float(input("What is your rent?\n"))
utilites = float(input("How much money do you pay for utilites?\n"))
groceries = float(input("How much money do you pay for groceries?\n"))
transportation = float(input("How much money do you pay for transportation?\n"))
savings = float(income-utilites-groceries-transportation)
spendings = float(utilites+groceries+transportation)

print("\n")

print("Thank you for trying me out! I hope I helped with your finacial needs.")

def info(cost, income, type):
    percent1 = rent/income *100
    print(f"Your {type} is {cost:.2} which is {percent1}% of your income.")

def info(cost, income, type):
    percent2 = utilites/income *100
    print(f"Your {type} is {cost:.2} which is {percent2}% of your income.")

def info(cost, income, type):
    percent3 = groceries/income *100
    print(f"Your {type} is {cost:.2} which is {percent3}% of your income.")

def info(cost, income, type):
    percent4 = transportation/income *100
    print(f"Your {type} is {cost:.2} which is {percent4}% of your income.")

def info(cost, income, type):
    percent5 = savings/income *100
    print(f"Your {type} is {cost:.2} which is {percent5}% of your income.")

def info(cost, income, type):
    percent6 = spendings/income *100
    print(f"Your {type} is {cost:.2} which is {percent6}% of your income.")