import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def main():
    for i in range(3):  # Roll dice three times
        die1, die2 = roll_dice()  # Local scope variables
        print(f"Roll {i+1}: Die 1 = {die1}, Die 2 = {die2}")

if __name__ == '__main__':
    main()
