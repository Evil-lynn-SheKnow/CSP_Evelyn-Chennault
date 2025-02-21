# Evelyn Chnenault, Name Decorator Python

str_one = "Would you like another version of your name decorated?"
str_two = "If yes, type you name. If no, leave the program."
name_four = name.strip().capitalize()

print("Hello, user! Welcome to the name decorator.")
name = input("What is your name?\n").strip().lower()

print("<<<", name, ">>>\n")

name_two = input(f"{str_one} {str_two}\n").strip().upper()

print("<--", name_two, "-<<\n")

name_three = input(f"{str_one} {str_two}\n").strip().upper()

print("(-_-)", name_three, "(^.^)\n")

print("Thank you for using this program, " + name_four)
print("I hope to see you again!")
print("Bye bye!")