side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

sides = [side1, side2, side3]
sides.sort()  # Sort the sides in ascending order

if (sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
