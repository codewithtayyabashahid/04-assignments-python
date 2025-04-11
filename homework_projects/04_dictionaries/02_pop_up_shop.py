def main():
    # Dictionary of fruits and their costs
    fruit_prices = {
        "apple": 1.5,
        "durian": 10.0,
        "jackfruit": 3.0,
        "kiwi": 2.5,
        "rambutan": 4.0,
        "mango": 2.0
    }

    total_cost = 0  # Initialize the total cost

    # Loop through the dictionary and ask for the quantity of each fruit
    for fruit, price in fruit_prices.items():
        # Ask how many of the fruit the user wants
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        
        # Add the cost of the selected fruit to the total cost
        total_cost += quantity * price

    # Print the total cost
    print(f"Your total is ${total_cost:.2f}")


if __name__ == '__main__':
    main()
