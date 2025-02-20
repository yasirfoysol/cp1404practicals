LOWER = 33
UPPER = 127

character = input("Enter a character: ")
print(f"The ASCII code for {character} is {ord(character)}")

number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
while number < LOWER or number > UPPER:
    number = int(input(f"Invalid! Enter a number between {LOWER} and {UPPER}: "))
print(f"The character for {number} is {chr(number)}")

# Printing ASCII table
for i in range(LOWER, UPPER + 1):
    print(f"{i:3} {chr(i)}")
