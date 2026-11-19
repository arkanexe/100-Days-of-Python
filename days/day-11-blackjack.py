import random


def deal_card():
    cards = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    return random.choice(cards)


def calculate_score(cards):
    # Blackjack
    if len(cards) == 2 and sum(cards) == 21:
        return 0

    # Change Ace from 11 to 1 if score goes over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "draw"

    elif computer_score == 0:
        return "loss"

    elif user_score == 0:
        return "win"

    elif user_score > 21:
        return "loss"

    elif computer_score > 21:
        return "win"

    elif user_score > computer_score:
        return "win"

    else:
        return "loss"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal two cards to each player
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # -------------------------
    # PLAYER'S TURN
    # -------------------------

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}")
        print(f"Your current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: "
            )

            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # -------------------------
    # COMPUTER'S TURN
    # -------------------------

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # -------------------------
    # FINAL RESULT
    # -------------------------

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print("\n========== FINAL RESULT ==========")
    print(f"Your final hand: {user_cards}")
    print(f"Your final score: {user_score}")

    print(f"Computer's final hand: {computer_cards}")
    print(f"Computer's final score: {computer_score}")

    result = compare(user_score, computer_score)

    if result == "win":
        print("🎉 You win!")

    elif result == "loss":
        print("You lose.")

    else:
        print("It's a draw.")

    return result


# =====================================
# MAIN GAME
# =====================================

chips = 100

wins = 0
losses = 0
draws = 0
plays = 0

print("================================")
print("       WELCOME TO BLACKJACK")
print("================================")
print(f"You start with {chips} chips.")


while chips > 0:

    print(f"\nYou currently have {chips} chips.")

    play_again = input("Do you want to play? Type 'y' or 'n': ").lower()

    if play_again != "y":
        break

    # -------------------------
    # GET BET
    # -------------------------

    while True:

        try:
            bet = int(input(f"How many chips do you want to bet? (1-{chips}): "))

            if bet <= 0:
                print("Your bet must be greater than 0.")

            elif bet > chips:
                print("You don't have enough chips.")

            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # -------------------------
    # PLAY GAME
    # -------------------------

    result = play_game()

    # -------------------------
    # UPDATE CHIPS + STATS
    # -------------------------

    if result == "win":

        wins += 1
        chips += bet

        print(f"\nYou won {bet} chips!")
        print(f"Your chips: {chips}")

    elif result == "loss":

        losses += 1
        chips -= bet

        print(f"\nYou lost {bet} chips.")
        print(f"Your chips: {chips}")

    else:

        draws += 1

        print("\nDraw — your bet is returned.")
        print(f"Your chips: {chips}")

    plays += 1


# =====================================
# FINAL STATISTICS
# =====================================

print("\n================================")
print("          GAME OVER")
print("================================")

print(f"Games played: {plays}")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print(f"Draws: {draws}")
print(f"Final chips: {chips}")

if plays > 0:
    win_rate = (wins / plays) * 100
    print(f"Win rate: {win_rate:.1f}%")

if chips == 0:
    print("You ran out of chips!")
else:
    print("Thanks for playing!")
