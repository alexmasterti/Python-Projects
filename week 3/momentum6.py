# Get mass from user input
mass = float(input("Enter the mass (in kg): "))
# Get velocity from user input
velocity = float(input("Enter the velocity (in m/s): "))

# Calculate kinetic energy
kineticEnergy = (mass * velocity ** 2) / 2

# Print the result
print("Kinetic Energy:", kineticEnergy)
