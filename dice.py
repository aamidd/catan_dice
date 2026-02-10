import random

def roll():
    return random.choice(range(6)) + 1

def query_number_of_players():
    number_of_players = int(input("> enter the number of players: "))
    while number_of_players > 6 or number_of_players < 1:
        print("!!! number of players should be between 1-6 !!!")
        number_of_players = int(input("> enter the number of players: "))
    return number_of_players

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
        d = [roll(), roll()] # dice

        print(players[curr_player].center(10, "*"))
        print(f"{d[0]} and {d[1]}")
        print(f"total: {d[0] + d[1]}")
        curr_player = (curr_player + 1) % n # add one to curr_player and roll back if it exceeds n
except KeyboardInterrupt:
    print()
