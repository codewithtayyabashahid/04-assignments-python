def double_numbers(numbers):
    return [num * 2 for num in numbers]

def main():
    try:
        user_input = input("Enter a list of numbers separated by spaces: ")
        number_list = [float(num) for num in user_input.split()]
        
        doubled_list = double_numbers(number_list)
        print(f"The doubled numbers are: {doubled_list}")
    except ValueError:
        print("Invalid input. Please enter numeric values separated by spaces.")

if __name__ == '__main__':
    main()