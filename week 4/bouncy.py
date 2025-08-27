initial_height = float(input("Enter the initial height from which the ball is dropped (in feet): "))
bounciness_index = float(input("Enter the bounciness index of the ball (between 0 and 1): "))
num_bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

total_distance = 0
for _ in range(num_bounces):
    total_distance += initial_height  # Distance from the current bounce
    initial_height *= bounciness_index  # Height of the next bounce
    total_distance += initial_height  # Distance from the next upward bounce

total_dist = round(total_distance, 2)
print(f"The total distance traveled by the ball after {num_bounces} bounces is {total_dist} feet.")
