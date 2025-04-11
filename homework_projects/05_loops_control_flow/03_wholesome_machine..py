def main():
    # The affirmation to be typed correctly
    affirmation = "I am capable of doing anything I put my mind to."
    while True:
        # Ask the user to type the affirmation
        user_input = input("Please type the following affirmation: ")
        
        if user_input == affirmation:
            print("That's right! :)")
            break  # Exit the loop if the affirmation is correct
        else:
            print("Hmmm That was not the affirmation.")

if __name__ == '__main__':
    main()
