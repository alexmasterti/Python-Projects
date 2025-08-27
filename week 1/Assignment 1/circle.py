#Page Title
print("Calculate the circle's area")

#Functions

#Function responsable to validate if the input is a float
def validateInputFloat(parameter):
    temp = input("Please informe the "+parameter+": ")

    while not temp.isdigit():
        temp = input("Please informe a valid "+parameter+": ")

    return float(temp)

#Function responsable to calculate the area of the circle
def calculateArea(r):    
    return 3.14 * r * r


radius = validateInputFloat("radius")

print("The area of the circle is: " + str(calculateArea(radius)))


    
    
    
