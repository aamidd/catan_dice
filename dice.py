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
        except ValueError:
            print("\n!!! enter a number !!!\n")
            continue
        if 1 <= n <= 6:
            return n
        print("\n!!! number of players should be between 1-6 !!!\n")

n = query_number_of_players() # number of players
players = []

print("\n*** enter the names of the players in the same order as you're sitting ***\n")
for i in range(n):
    players += [input(f"player no.{i + 1}: ")]
    
# Choose a player randomly
print("\nrandomly choosing the first player...")
curr_player = random.randrange(n)
print(f"{players[curr_player]} was chosen")
print("\n*** hit enter to roll the dice or hit q and enter to quit ***\n")

max_width = max(len(p) for p in players) + 6

while True:
    cmd = input().strip().lower()
    if cmd == "q":
        print("\n*** quitting ***\n")
        break

    d1, d2, total = roll_two()

    print(f" {players[curr_player]} ".center(max_width, "*"))
    print(f"{d1} and {d2}")
    print(f"total: {total}")
    curr_player = (curr_player + 1) % n # add one to curr_player and roll back if it exceeds n
