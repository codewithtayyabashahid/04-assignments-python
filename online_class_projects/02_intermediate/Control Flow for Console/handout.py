import random

NUM_ROUNDS = 5

def play_high_low():
    """Plays the High-Low game for a specified number of rounds."""
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    player_score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num}")
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        print(f"Your number is {player_number}")

        while True:
            user_guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
            if user_guess in ["higher", "lower"]:
                break
            else:
                print("Please enter either 'higher' or 'lower'.")

        print(f"The computer's number was {computer_number}")

        if (user_guess == "higher" and player_number > computer_number) or \
           (user_guess == "lower" and player_number < computer_number):
            print("You were right!")
            player_score += 1
        else:
            print("Aww, that's incorrect.")

        print(f"Your score is now {player_score}")

    print("\nThanks for playing!")

    # Extension #2: Conditional ending messages
    if player_score == NUM_ROUNDS:
        print("\nWow! You played perfectly!")
    elif player_score >= NUM_ROUNDS // 2:
        print("\nGood job, you played really well!")
    else:
        print("\nBetter luck next time!")

if __name__ == "__main__":
    play_high_low()