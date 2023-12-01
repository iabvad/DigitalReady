import sys, random, pyfiglet

# The main idea of the Class below allows us to form the Basics of the whole code and how we will be able 
# to tell the difference between the values, players and face (Which will differ based on face).
class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# 
def pick_a_card():
    suit = random.choice(["♦️", "♠️", "♥️", "♣️"])
    rank = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"])
    return Card(suit, rank)

# function that sets the players score after evey action
def calculate_score(cards):
    score = 0
    ace_count = 0

    # sets the values for each card
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
    worl = [[] for _ in range(players)]
    # Initial deal
    for j in range(players):
        hands[j].append(pick_a_card())

    # Game loop
    for i in range(players):
        while True:
            print(f"Player {i + 1} has just drawn a {hands[i][-1]}")
            score = calculate_score(hands[i])
            print(f"Player {i + 1} score: {score}")

            if score == 21:
                print(f"Player {i + 1} has a Blackjack!")
                result1 = pyfiglet.figlet_format(f"Player {i + 1} Wins") 
                print(result1) 
                break

            if score > 21:
                print(f"Player {i + 1} busts with a score of {score}!")
                result2 = pyfiglet.figlet_format(f"Player {i + 1} Loses") 
                print(result2) 
                break

            choice = input("Player " + str(i + 1) + ", hit or stand? ").lower()
            if choice == "hit":
                hands[i].append(pick_a_card())
            elif choice == "stand":
                break
            else:
                print("Invalid choice. Please enter 'hit' or 'stand'.")

if __name__ == "__main__":
    go(int(sys.argv[1]))
