def sum_numbers(numbers):
    return sum(numbers)

def main():
    try:
        user_input = input("Enter a list of numbers separated by spaces: ")
        number_list = [float(num) for num in user_input.split()]
        
        total = sum_numbers(number_list)
        print(f"The sum of the numbers is: {total}")
    except ValueError:
        print("Invalid input. Please enter numeric values separated by spaces.")

if __name__ == '__main__':
    main()