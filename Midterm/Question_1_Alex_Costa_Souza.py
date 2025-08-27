# Q1 - Body Mass Index Calculator
	
#BMI Categories:
#Underweight = <18.5
#Normal weight = 18.5–24.9
#Overweight = 25–29.9
#Obesity = BMI of 30 or greater

def getBMICategories(bmi):
    if bmi < 18.5:
         return "Underweight"
    elif bmi > 18.5 and bmi < 24.9:
         return "Overweight"
    elif bmi > 30:
         return "Obesity"

weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

bmi = 703 * (weight / (height ** 2))
print("Your Body Mass Index is:", bmi)
print("Your are ", getBMICategories(bmi))
