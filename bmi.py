height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

height = height / 100

bmi = int(weight / (height ** 2))

print(f'Your BMI is {bmi}')