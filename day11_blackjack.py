from art import logo
import random

def deal_card(cards):
    card = random.choice(cards)
    return card

def calculate_score(hand):
    score = sum(hand)

    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)

    return score

def check_score(p, d):
    player_score = calculate_score(p)
    dealer_score = calculate_score(d)

    print(f"Your final hand: {p}, final score: {player_score}.")
    print(f"Computer's final hand: {d}, final score: {dealer_score}.")

    if player_score > 21:
        return "You went over, you lose."
    if dealer_score > 21:
        return "Dealer went over, you win."
    if player_score == dealer_score:
        return "It's a draw."
    if player_score == 21 and len(p) == 2:
        return "Blackjack! You win."
    if dealer_score == 21 and len(d) == 2:
        return "Dealer has Blackjack. You lose."
    if player_score > dealer_score:
        return "You win!"

    return "You lose!"

def main():
    while True:
        game_on = input("Would you like to play BlackJack? Type 'y' or 'n': ").lower()
        print()
        if game_on == "n":
            break
        if game_on == "y":
            deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            print(logo)
            player = []
            dealer = []
            while len(player) < 2 and len(dealer) < 2:
                dealer.append(deal_card(deck))
                player.append(deal_card(deck))

            print(f"Your cards: {player}, current score {calculate_score(player)}.")
            print(f"Computer's first card: {dealer[0]}")
            if calculate_score(player) == 21 or calculate_score(dealer) == 21:
                #print(check_score(player, dealer))
                continue

            while calculate_score(player) < 21:
                new_card = input("Type 'y' to get another card, type 'n' to stop: ").lower()
                if new_card == "y":
                    player.append(deal_card(deck))
                    print(f"Your cards: {player}, current score {calculate_score(player)}.")
                    if calculate_score(player) > 21:
                        #print(check_score(player, dealer))
                        break

                elif new_card == "n":
                    break
                else:
                    print("Invalid input, please try again.")
            if calculate_score(player) > 21:
                print(check_score(player, dealer))
            else:
                while calculate_score(dealer) < 17:
                    dealer.append(deal_card(deck))
                print(check_score(player, dealer))

        else:
            exit()


while __name__ == "__main__":
    main()