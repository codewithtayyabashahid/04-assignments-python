def print_multiple(message, repeats):
    """Prints the message the specified number of times on the same line."""
    for _ in range(repeats):
        print(message, end=" ")  # Print message with a space, no newline
    print()  # Print a newline at the end

def main():
    # Get input from user
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    
    print_multiple(message, repeats)


if __name__ == '__main__':
    main()
