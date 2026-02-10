import random

def roll():
    return random.choice(range(6)) + 1

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
        d = [roll(), roll()] # dice

        print(players[curr_player].center(10, "*"))
        print(f"{d[0]} and {d[1]}")
        print(f"total: {d[0] + d[1]}")
        curr_player = (curr_player + 1) % n # add one to curr_player and roll back if it exceeds n
except KeyboardInterrupt:
    print()
