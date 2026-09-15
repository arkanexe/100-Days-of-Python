# enemies = 1
# def increase_enemies():
#     print(f"enemies inside function: {enemies}")

#     return enemies + 1

# enemies = increase_enemies()
# print(f"enemies ouside function: {enemies}")

import random
print("Welcome to the Number Guessing Game! ")
print("I am thinking of a number between 1 and 100.")
attempt = 0
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == 'easy':
    attempt = 10
elif level == "hard":
    attempt = 5
else:
    print("You picked a wrong section")
    exit()

random_number = random.randint(1, 100)

def compare (guess, number):
    if guess > number:
        return "Too High"
    elif guess == number:
        return "Correct"
    else:
        return "Too Low"

while attempt != 0:
    print(f"You have {attempt} attempts remaining to guess the number")
    guess = int(input("Make a Guess: "))
    result = compare(guess, random_number)
    print(result)

    if result == "Correct":
        break
    else:
        attempt -= 1

        if attempt > 0:
            print("Guess again")
else:
    print(f"You've run out of guesses, you lose. the answer was {random_number}")
