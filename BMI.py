# write a program to calculate BMI 

# Declare Variable and accept user input

h = float(input("Enter Height (in m) => "))
w = float(input("Enter Weight (in kg) => "))

# Calculating BMI (bmi)

bmi = w/(h**2)

# Range of BMI

# Print BMI
print("Your BMI (in kg/m2 ) is",bmi)

# BMI of 25 or more is Overweight
if bmi >= 25.0:
    print("Overweight")

# BMI of 18.5 or less is Underweight
elif bmi < 18.5:
    print("Underweight")

# BMI of 18.6 to 24.9 is Healthy
else:
    print("Healthy")
