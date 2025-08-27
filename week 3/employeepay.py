# Get regular hours, overtime hours, and wage from user input
regularHours = float(input("Enter the number of regular hours worked: "))
overtimeHours = float(input("Enter the number of overtime hours worked: "))
wage = float(input("Enter the wage per hour: "))

# Calculate regular pay
regularPay = regularHours * wage

# Calculate overtime pay
overtimePay = overtimeHours * wage * 1.5

# Calculate total pay
totalpay = regularPay + overtimePay

# Print the result
print("Total Pay: ", totalpay)
