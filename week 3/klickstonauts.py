# Get klicks from user input
klicks = float(input("Enter the distance in klicks: "))

# Calculate nauts
nauts = klicks * 90 * 60 / 10000.0

# Print the result
print("Nauts:", nauts)
