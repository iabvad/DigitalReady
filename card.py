import sys, random
# The main idea of the Class below allows us to form the Basics of the whole code and how we will be able 
# to tell the difference between the values, players and face (Which will differ based on face).

class Card:
    def __init__(self, face: list, value: list, player: str):
        self.face = face
        self.value = value
        self.player = player

    def pick_a_card(): 
        card = random.choices(cards) 
        rank = random.choices(ranks) 
        return "The " + rank + " of " + card

# These Objects will tell us which cards will be used in the game, based on the card and its type, we can 
# determine the value and add it to the total count.
cards = ["♦️", "♠️", "♥️", "♣️"] 
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]



# How the code will pick a randomized card to be played.

def go(num_players: int):

    players = str(num_players)
    print("Number of Players: " + players)
    while True:
        scores = []
        for i in range(1, num_players, 1):
            choice = input("Player " + i +", hit or stand?")
            if choice is "hit" or "Hit:":
                print(pick_a_card())
                if isinstance(int, rank):

                elif isinstance(str, rank) and len(rank) >= 4:

            
if __name__ == "__name__":
    go(sys.argv[1])
