#Get user input for weight and height
weight = float(input("Enter your weight in kilograms:"))
height = float(input("Enter your height in meters:"))

#Calculate BMI
bmi = weight /(height ** 2)

#classifyinf BMI into some categories
if bmi < 18.5:
    category = "You are Underweight"
elif bmi < 25:
    category = "You are normal"
elif bmi < 90:
    category = "You are Overweight"
else:
    category = "Obese"

#Displays the results
print(f"Your BMI is: {bmi:.2f}")
print(f"Your category is: {category}")

#Ask user if they want to try another BMI
response = input("Do you want to Try another BMI? (yes/no):")

#Exit if user says no
if response.lower() == "no":
    print("Jai Shree Ram")






