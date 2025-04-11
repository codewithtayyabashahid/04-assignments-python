def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high

def main():
    # Prompt user for input
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    
    if in_range(n, low, high):
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    main()
