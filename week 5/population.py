# Inputs
initial_population = int(input("Enter the initial number of organisms: "))
growth_rate = float(input("Enter the rate of growth (a float > 1): "))
growth_period = int(input("Enter the number of hours to achieve the rate: "))
hours = int(input("Enter the number of hours of growth: "))

# Calculate and output the total population
doublings = hours // growth_period

# Calculate the final population
final_population = initial_population * (growth_rate ** doublings)

# Cast to int
total_population = int(final_population)
    
print("Total population after {} hours: {}".format(hours, total_population))
