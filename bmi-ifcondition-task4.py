height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    category = "Obesity"
elif bmi >= 25:
    category = "Overweight"
elif bmi >= 18.5:
    category = "Normal"
else:
    category = "Underweight"

print("BMI:", round(bmi, 2))
print("Category:", category)
