# Milestone #1: Mars Weight

# We use constants for better readability and maintainability
MARS_GRAVITY_FACTOR = 0.378

def calculate_mars_weight():
    """Calculates and prints the equivalent weight on Mars."""
    try:
        earth_weight_str = input('Enter a weight on Earth (in kg or lbs): ')
        earth_weight = float(earth_weight_str)
        mars_weight = earth_weight * MARS_GRAVITY_FACTOR
        rounded_mars_weight = round(mars_weight, 2)
        print(f'The equivalent weight on Mars: {rounded_mars_weight}')
    except ValueError:
        print("Invalid input. Please enter a numeric weight.")

if __name__ == '__main__':
    calculate_mars_weight()

    # Milestone #2: Planetary Weights

# Define gravity factors as constants for each planet relative to Earth
GRAVITY_FACTORS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.360,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.140
}

def calculate_planetary_weight():
    """Calculates and prints the equivalent weight on a specified planet."""
    try:
        earth_weight_str = input("Enter a weight on Earth (in kg or lbs): ")
        earth_weight = float(earth_weight_str)
        planet = input("Enter a planet (e.g., Mars, Jupiter): ")

        if planet in GRAVITY_FACTORS:
            gravity_factor = GRAVITY_FACTORS[planet]
            planetary_weight = earth_weight * gravity_factor
            rounded_planetary_weight = round(planetary_weight, 2)
            print(f"The equivalent weight on {planet}: {rounded_planetary_weight}")
        else:
            print(f"Sorry, information for the planet '{planet}' is not available.")
    except ValueError:
        print("Invalid input. Please enter a numeric weight.")

if __name__ == "__main__":
    calculate_planetary_weight()