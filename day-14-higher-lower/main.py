from data import data
import random

def pick_account():
    return random.choice(data)

def check_account(guess, account_a, account_b):
    if account_a["follower_count"] > account_b["follower_count"]:
        return guess == "A"
    else:
        return guess == "B"

accountA = pick_account()
accountB = pick_account()

while accountB == accountA:
    accountB = pick_account()


game_should_continue = True
score = 0

while game_should_continue:
    print(f"Comapare A: {accountA["name"]}, {accountA["description"]}")
    print(f"Against B: {accountB["name"]}, {accountB["description"]}")

    guess = input("Who has more followers? Type 'A' or 'B': ")
    is_correct = check_account(guess, accountA, accountB)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")

        accountA = accountB
        accountB = pick_account()

        while accountA == accountB:
            accountB = pick_account()
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
    print(accountA)
