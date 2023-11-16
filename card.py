import sys, random

class Card:
    def __init__(self, face: str, value: int, player: str):
        self.face = face
        self.value = value
        self.player = player

cards = ["♦️", "♠️", "♥️", "♣️"] 
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]




def pick_a_card(): 
    card = random.choices(cards) 
    rank = random.choices(ranks) 
    return "The " + rank + " of " + card 

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
