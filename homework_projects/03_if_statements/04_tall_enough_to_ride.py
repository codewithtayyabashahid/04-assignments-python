def main():
    MIN_HEIGHT = 50  # Minimum height requirement

    while True:
        height = input("How tall are you? (Press enter to quit) ")

        if height == "":
            print("Goodbye!")
            break
        
        try:
            height = float(height)
            if height >= MIN_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()
