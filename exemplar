import sys
import random

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

def go(num_players):
    players = int(num_players)
    print("Number of Players: " + str(players))

    # Initialize players' hands
    hands = [[] for _ in range(players)]

    # Initial deal
    for i in range(players):
        for _ in range(2):
            hands[i].append(pick_a_card())

    # Game loop
    for i in range(players):
        while True:
            print(f"Player {i + 1} hand: {[str(card) for card in hands[i]]}")
            choice = input("Player " + str(i + 1) + ", hit or stand? ").lower()
            if choice == "hit":
                hands[i].append(pick_a_card())
                score = calculate_score(hands[i])
                print(f"Player {i + 1} new card: {str(hands[i][-1])}")
                if score > 21:
                    print(f"Player {i + 1} busts with a score of {score}!")
                    break
            elif choice == "stand":
                break
            else:
                print("Invalid choice. Please enter 'hit' or 'stand'.")

if __name__ == "__main__":
    go(int(sys.argv[1]))
