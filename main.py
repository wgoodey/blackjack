############### Blackjack Project #####################
import random
import os
import art

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


hand = []
dealer_hand = []


def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def hit(players_hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    players_hand.append(random.choice(cards))


def check_is_bust(players_hand):
    return sum(players_hand) > 21


def review_cards(players_hand):
    if players_hand == hand:
        player = "Your"
    else:
        player = "The dealer's"
    print(f"{player} cards are {players_hand}")


def reduce_ace(players_hand):
    pos = 0
    for card in players_hand:
        if card == 11:
            hand[pos] = 1
            review_cards(players_hand)
            break
        else:
            pos += 1
    return sum(players_hand)


def initial_deal():
    dealer_hand.clear()
    hit(dealer_hand)
    hit(dealer_hand)
    hand.clear()
    hit(hand)
    hit(hand)


game_over = False
play_again = True
while play_again:
    initial_deal()
    score = sum(hand)
    dealer_score = sum(dealer_hand)

    while dealer_score < 17:
        hit(dealer_hand)
        dealer_score = sum(dealer_hand)

    print(art.logo)
    print("Welcome to Blackjack! The table is all set up.\n")
    print(f"The dealer's first card is {dealer_hand[0]}.\n")
    print(f"Your initial hand is {hand}.")

    # a blackjack means instant stay
    if score == 21 and len(hand) == 2:
        print("You got a blackjack!")
        game_over = True

    while not game_over:
        deal_again = input(f"Your total is: {sum(hand)}. Type \'hit\' to deal again or \'stay\' to keep your "
                           f"hand as it is.\n").lower()
        if deal_again == "hit":
            hit(hand)
            print()
            review_cards(hand)
            score = sum(hand)
            # check for aces
            if score > 21:
                if 11 in hand:
                    # reduce an ace to 1
                    score = reduce_ace(hand)
                else:
                    game_over = check_is_bust(hand)
                    print(f"Bad luck, with {score} you've gone over 21.")
        else:
            break

    score = sum(hand)
    dealer_bust = check_is_bust(dealer_hand)
    bust = check_is_bust(hand)

    review_cards(dealer_hand)
    print(f"The dealer's total is {dealer_score}.")

    if score == dealer_score:
        print("It's a draw.")
    elif score == 21 and len(hand) == 2:
        print("You win!")
    elif not bust:
        if not dealer_bust and score > dealer_score:
            print("Congratulations, you win.")
    elif dealer_bust:
        print("You both busted, so you both lose.")
    else:
        print("You lose.")

    choice = input("\nPlay again?\n").lower()
    if choice == "yes":
        clear_screen()
    else:
        play_again = False
