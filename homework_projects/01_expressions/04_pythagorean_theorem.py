import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    try:
        ab = float(input("Enter the length of AB: "))
        ac = float(input("Enter the length of AC: "))
        
        if ab <= 0 or ac <= 0:
            print("Lengths must be positive numbers.")
            return
        
        bc = calculate_hypotenuse(ab, ac)
        print(f"The length of BC (the hypotenuse) is: {bc}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == '__main__':
    main()
