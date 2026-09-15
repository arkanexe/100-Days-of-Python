import random

def deal_card ():
    cards = [11, 10, 10, 10, 9, 8, 7, 5, 4, 3, 2]
    return random.choice(cards)
user_win = True

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponentt has BlackJack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "computer Lost you win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You Lose"
def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

print("Welcome to Blackjack!")
print("You have 100 chips.")

wins = 0
losses = 0
draws = 0
plays = 0
chips = 100


def play_game():

    computer_card = []
    user_card = []
    is_game_over = False

    for _ in range(2):
        computer_card.append(deal_card())
        user_card.append(deal_card())



    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)


        print(f"Your cards: {user_card}, current_score: {user_score}")
        print(f"computer first card: {computer_card}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to deal another card ")
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
            computer_card.append(deal_card())
            computer_score = calculate_score(computer_card)

    print(f"Your final hand: {user_card} final_score: {user_score}")
    print(f"Your computer hand: {computer_card} final_score: {computer_score}")
    print(compare(user_score, computer_score))

    if 'win' in compare(user_score, computer_score):
        wins += 1
        print(f"You bet: {bet}")
        print(f"You Won: {bet}")
        print(f"Your chips: {chips + bet}")
    elif "draw" in compare(user_score, computer_score):
        print("Draw!")
        draws += 1
        print(f"Your chips remain: {chips}")
    else:
        losses += 1
        print(f"You bet: {bet}")
        print(f"You Lost: {bet}")
        print(f"Your chips: {chips - bet}")

while input("Do you want to play? ") == "y":
    bet = int(input("How many chips do you want to bet? "))

    if type(bet) is not int:
        print(f"Please enter a valid input ")
        bet = int(input("How many chips do you want to bet? enter an appropriate figure"))
    if bet > chips:
        print("You don't have enough chips.")
        bet = int(input("How many chips do you want to bet? enter an appropriate figure"))
    else:
        play_game()
        plays += 1


if plays >= 1:
    print("===== STATISTICS =====")
    print(f"Games: {plays}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Draws: {draws}")
    print(f"Win rate: {(wins / plays) * 100}")
