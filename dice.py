#!/opt/homebrew/bin/python3
import random

def roll():
    return random.choice(range(6)) + 1

player1 = input("enter first player's name: ")
player2 = input("enter second player's name: ")
print()
print("randomizing the first player...")

curr_player = random.choice([player1, player2])
print(f"{curr_player} was chosen")

try:
    while True:
        input()
        d1 = roll()
        d2 = roll()
        print(curr_player.center(10, "*"))
        print(f"{d1} and {d2}")
        print(f"total: {d1 + d2}")
        curr_player = player2 if curr_player == player1 else player1
except KeyboardInterrupt:
    print()
