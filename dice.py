import random

def roll_dice():
    print("🎲 Rolling the dice...")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"You rolled: {dice1} and {dice2}")
    if dice1 == dice2:
        print("Double! 🎉")

# Run the function
roll_dice()
