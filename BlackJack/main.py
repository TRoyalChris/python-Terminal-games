import random
#import BlackJack

# Cards: these can repeat
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
cpu_cards = []
player_total = 0
cpu_total = 0
finish = False


def clear_cards():
    """This function clears the cards from the lists to restart the game"""
    player_cards.clear()
    cpu_cards.clear()
    for card in range(2):
        player_cards.append(random.choice(cards))
        cpu_cards.append(random.choice(cards))


print(BlackJack.ascii_art)
start_game = input("Welcome to blackjack, want to play a quick game? Y/N:\n").lower()

if start_game == "y":
    clear_cards()

    for card in player_cards:
        player_total += card
    for card in cpu_cards:
        cpu_total += card

    print(f"This is the PLAYERS hand:\n{player_cards} (Total: {player_total})")
    print(f"This is the CPU hand:\n{cpu_cards[0]}, X")

    if player_total == 21:
        more_cards = "n"
    else:
        more_cards = input("Would you like another card? Y/N\n").lower()

    while not finish:
        if more_cards == "y":
            player_cards.append(random.choice(cards))
            print(f"This is the PLAYERS hand:\n{player_cards}")
            player_total += player_cards[-1]

            while player_total > 21 and 11 in player_cards:
                ace_position = player_cards.index(11)
                player_cards[ace_position] = 1
                player_total = sum(player_cards)

            if player_total > 21:
                print(f"Your total is over 21, you lose! TOTAL: {player_total}")
                print(f"The CPU's total was: {cpu_total}")
                print(f"CPU's cards: {cpu_cards}")
                finish = True
            elif player_total < 21:
                more_cards = input(
                    f"Your total in cards is of {player_total}, would you like another card? Y/N\n").lower()
                if more_cards == "y":
                    continue
                else:
                    print(f"Very well, your total was: {player_total}")
                    finish = True
            else:
                print(f"Hit 21! Your TOTAL: {player_total}")
                finish = True
        else:
            print(f"Very well, your TOTAL: {player_total}")
            finish = True

    if player_total <= 21:
        print("\n--- CPU's Turn ---")
        print(f"CPU reveals cards: {cpu_cards} | Starting Total: {cpu_total}")

        while cpu_total < 17:
            cpu_cards.append(random.choice(cards))
            cpu_total += cpu_cards[-1]
            print(f"CPU hits and draws a {cpu_cards[-1]}. Current Hand: {cpu_cards}")

            while cpu_total > 21 and 11 in cpu_cards:
                ace_position = cpu_cards.index(11)
                cpu_cards[ace_position] = 1
                cpu_total = sum(cpu_cards)

        print(f"CPU stands. Final Hand: {cpu_cards} | Final Total: {cpu_total}\n")

        print("=" * 30)
        if cpu_total > 21:
            print(f"CPU busted with {cpu_total}! Player wins!")
        elif player_total > cpu_total:
            print(f"Player has {player_total} vs CPU's {cpu_total}. Player wins!")
        elif cpu_total > player_total:
            print(f"CPU has {cpu_total} vs Player's {player_total}. CPU wins! 🏛")
        else:
            print(f"Both have {player_total}. It's a Draw!")
        print("=" * 30)

else:
    print("Thanks for passing by, see you around!")