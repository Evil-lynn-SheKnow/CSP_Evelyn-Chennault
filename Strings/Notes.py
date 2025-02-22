# Evelyn Chnenault, Strings Notes Python

# strings are a data type that holds any info surrounded by quotation marks "" ''

# note = "Ms. LaRose's class"

name = input("What is your first name?\n").strip().capitalize()

print(f"Hello, {name}. Welcome to my program!")

# print("This is your name: "+ name)

sentence = "The quick brown fox jumps over the lazy dog"

# print(len(sentence))
# print(sentence[4])
start = sentence.find("brown")
length = len("brown fox")
print(sentence[start:start+length])