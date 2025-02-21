# Evelyn Chnenault, Name Decorator Python

str_one = "Would you like another version of your name decorated?"
str_two = "Just type your name in again!"

print("Hello, user! Welcome to the name decorator.")
name = input("What is your name?\n").strip().lower()

print("<<<", name, ">>>\n")

name_two = input(f"{str_one} {str_two}\n").strip().upper()

print("<--", name_two, "-<<\n")

name_three = input(f"{str_one} {str_two}\n").strip().upper()

print("(-_-)", name_three, "(^.^)\n")


name_four = name.strip().capitalize()
print("Thank you for using this program, " + name_four + ".")
print("Bye bye!")