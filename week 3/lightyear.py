# Define seconds in a year and rate
seconds_in_a_year = 365 * 24 * 60 ** 2
rate = 3 * 10 ** 8  # meters per second

# Calculate
distance = rate * seconds_in_a_year

# Print the result
print("Distance traveled in a year:", distance, "meters")
