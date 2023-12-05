import sys
import random
import pyfiglet

class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

def pick_a_card():
    suit = random.choice(["♦️", "♠️", "♥️", "♣️"])
    rank = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"])
    return Card(suit, rank)

def calculate_score(cards):
    score = 0
    ace_count = 0

    for card in cards:
        if isinstance(card.rank, int):
            score += card.rank
        elif card.rank in ["Jack", "Queen", "King"]:
            score += 10
        elif card.rank == "Ace":
            ace_count += 1
            score += 11
        else:
            print("Invalid card rank.")

    while ace_count > 0 and score > 21:
        score -= 10
        ace_count -= 1

    return score

def print_player_status(player_num, card):
    print(f"Player {player_num} has just drawn a {card}")

def print_player_score(player_num, score):
    print(f"Player {player_num} score: {score}")

def input_player_choice(player_num):
    return input(f"Player {player_num}, hit or stand? ").lower()

def print_winner_message(winners):
    if len(winners) > 1:
        string1 = ', '.join(map(str, winners))
        wins = pyfiglet.figlet_format(f"Players {string1} Have Won")
    else:
        wins = pyfiglet.figlet_format(f"Player {winners[0]} Has Won")

    print(wins)

def print_loser_message(losers):
    if len(losers) > 1:
        string2 = ', '.join(map(str, losers))
        losses = pyfiglet.figlet_format(f"Players {string2} Have Lost")
    else:
        string2 = ' '.join(map(str, losers))
        losses = pyfiglet.figlet_format(f"Player {string2} Has Lost")

    print(losses)

def determine_winner(stand_players, stand_values, losers):
    if len(stand_players) >= 1:
        standnum = stand_players[0]
        largest = stand_values[0]
        for i in range(1, len(stand_values)):
            if stand_values[i] > largest:
                losers.append(stand_players[i])
                largest = stand_values[i]
                standnum = stand_players[i]
            else:
                losers.append(stand_players[i])

        wins = pyfiglet.figlet_format(f"Player {standnum} Has Won")
        print(wins)

def go(num_players):
    players = int(num_players)
    print("Number of Players: " + str(players))

    winners = []
    losers = []

    hands = [[] for _ in range(players)]

    for j in range(players):
        hands[j].append(pick_a_card())

    stand_values = []
    stand_players = []

    for i in range(players):
        while True:
            pnum = i + 1
            print_player_status(pnum, hands[i][-1])
            score = calculate_score(hands[i])
            print_player_score(pnum, score)

            if score == 21:
                print(f"Player {pnum} has a Blackjack!")
                winners.append(pnum)
                break

            if score > 21:
                print(f"Player {pnum} busts with a score of {score}!")
                losers.append(pnum)
                break

            choice = input_player_choice(pnum)
            if choice == "hit":
                hands[i].append(pick_a_card())
            elif choice == "stand":
                stand_players.append(pnum)
                stand_values.append(score)
                break
            else:
                print("Invalid choice. Please enter 'hit' or 'stand'.")

    if len(winners) > 0:
        print_winner_message(winners)
    else:
        determine_winner(stand_players, stand_values, losers)

    if len(losers) > 0:
        print_loser_message(losers)

if __name__ == "__main__":
    go(int(sys.argv[1]))
