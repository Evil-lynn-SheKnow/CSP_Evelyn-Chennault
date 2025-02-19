# Evelyn Chnenault, Name Decorator Python

str_one = "Would you like another version of your name decorated?"
str_two = "If yes, type you name. If no, leave the program."

print("Hello, user! Welcome to the name decorator.")
name = input("What is your name?\n").strip().lower()

print("<<<", name, ">>>\n")

nameTwo = input(f"{str_one} {str_two}\n").strip().upper()

print("<--", nameTwo, "-<<\n")

nameThree = input(f"{str_one} {str_two}\n").strip().upper()

print("(-_-)", nameThree, "(^.^)\n")

print("Thank you for using this program!")
print("I hope to see you again!")
print("Bye bye!")