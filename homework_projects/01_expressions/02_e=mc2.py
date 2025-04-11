def main():
    C = 299792458  # Speed of light in meters per second
    
    while True:
        try:
            mass = float(input("Enter kilos of mass (or a negative number to quit): "))
            if mass < 0:
                print("Exiting program.")
                break
            
            energy = mass * C**2  # E = m * C^2
            
            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s")
            print(f"{energy} joules of energy!\n")
        
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == '__main__':
    main()