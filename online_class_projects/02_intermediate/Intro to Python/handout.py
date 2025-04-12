# Milestone #1: Mars Weight

earth_weight = float(input("Enter a weight on Earth: "))
mars_weight_percentage = 0.378
mars_weight = round(earth_weight * mars_weight_percentage, 2)

print("The equivalent on Mars:", mars_weight)

# Milestone #2: Adding in All Planets

earth_weight = float(input("Enter a weight on Earth: "))
planet = input("Enter a planet: ")

gravity_constants = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.360,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.140
}

if planet in gravity_constants:
    planet_weight = round(earth_weight * gravity_constants[planet], 2)
    print("The equivalent weight on", planet + ":", planet_weight)