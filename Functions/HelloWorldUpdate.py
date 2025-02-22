#Evelyn Chennault - Hello World Update Python

def hello(name):
    return input("What is your name?\n").strip().capitalize()
    
name = hello("name")

print(f"Your name is {name}. Hello, {name}!")