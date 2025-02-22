#Evelyn Chennault - Hello World Update Python

print("Hello, user. Teach me some fun names! Please give me five!")

def hello(name):
    return input(f"Please give me a {name}\n").strip().capitalize()
    
name = hello("name")
name_two = hello("name")
name_three = hello("name")
name_four = hello("name")
name_five = hello("name")

print(f"A cool name is {name}.")
print(f"A funny name is {name_two}.")
print(f"A scary name is {name_three}.")
print(f"A cute name is {name_four}.")
print(f"A normal name is {name_five}.")
print(f"I like the name {name_five}. I am going to call you {name_five}. Hello, {name}!")