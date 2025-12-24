import random
##tracks player gold between hits
try:
    with open("player_gold.txt", "r") as file:
        total_player_gold = int(file.read())
except FileNotFoundError:
    total_player_gold = 0

##generates a number between 1 and 20 and prints result
def dice_roll(i):
    roll = random.randint(1, 20)
    print(f"You rolled a {roll}!")
    player_attack(roll)

##prints outcome of dice roll and rewards player accordingly
def player_attack(attack):
    global total_player_gold
    if attack >=15:
        gold_found = monster_gold()
        total_player_gold = total_player_gold + gold_found
        with open("player_gold.txt", "w") as file:
            file.write(str(total_player_gold))
        print("That's a hit!")
        print(f"You found {gold_found} gold coins")
        print(f"Total gold: {total_player_gold}")
        
    else:
        print("Misfire!")

##generates a random amount of money for player reward
def monster_gold():
    return random.randint(1, 50)

dice_roll('')


