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

print("\n")

print("Thank you for trying me out! I hope I helped with your finacial needs.")

def info(cost, income, type):
    percent1 = rent/income *100
    print(f"Your {type} is {cost:.2} which is {percent1}% of your income.")

def info(cost, income, type):
    percent2 = utilites/income *100
    print(f"Your {type} is {cost:.2} which is {percent2}% of your income.")

def info(cost, groceries, type):
    percent3 = utilites/income *100
    print(f"Your {type} is {cost:.2} which is {percent3}% of your income.")

def info(cost, transportation, type):
    percent4 = utilites/income *100
    print(f"Your {type} is {cost:.2} which is {percent4}% of your income.")

def info(cost, income, type):
    percent5 = utilites/income *100
    print(f"Your {type} is {cost:.2} which is {percent5}% of your income.")