def main():
    try:
        num1 = int(input("Please enter an integer to be divided: "))
        num2 = int(input("Please enter an integer to divide by: "))
        
        if num2 == 0:
            print("Division by zero is not allowed.")
            return
        
        quotient = num1 // num2
        remainder = num1 % num2
        
        print(f"The result of this division is {quotient} with a remainder of {remainder}")
    except ValueError:
        print("Invalid input. Please enter integer values.")

if __name__ == '__main__':
    main()