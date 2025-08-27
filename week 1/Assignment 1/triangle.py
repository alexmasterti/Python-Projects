#Page Title
print("Calculate the triangle's area")

#Functions

#Function responsable to validate if the input is a Float
def validateInputFloat(parameter):
    temp = input("Please informe the "+parameter+": ")

    while not temp.isdigit():
        temp = input("Please informe a valid "+parameter+": ")

    return float(temp)

#Function responsable to calculate the area of the triangle
def calculateArea(b, h):    
    return 0.5 * b * h


base = validateInputFloat("base")
height = validateInputFloat("height")

print("The area of the triangle is: " + str(calculateArea(base, height)))


    
    
    
