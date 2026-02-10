import random

# rolls one die (random number between 1-6)
def roll():
    return random.randint(1, 6)

# roll two dice and returns them and their total
def roll_two():
    d1, d2 = roll(), roll()
    return d1, d2, d1 + d2

def query_number_of_players():
    while True:
        raw_input = input("> enter the number of players: ")
        try:
            n = int(raw_input)
        except:
            print("!!! enter a number !!!")
            continue
        if 1 <= n <= 6:
            return n
        print("!!! number of players should be between 1-6 !!!")

n = query_number_of_players() # number of players
players = []

print("*** enter the names of the players in the same order as you're sitting ***")
for i in range(n):
    players += [input(f"player no.{i + 1}: ")]
    
print()
# Choose a player randomly
print("randomly choosing the first player...")
curr_player = random.randrange(n)
print(f"{players[curr_player]} was chosen")
print("hit enter to roll the dice")

try:
    while True:
        input()
        d1, d2, total = roll_two()

        print(players[curr_player].center(10, "*"))
        print(f"{d1} and {d2}")
        print(f"total: {total}")
        curr_player = (curr_player + 1) % n # add one to curr_player and roll back if it exceeds n
except KeyboardInterrupt:
    print()
