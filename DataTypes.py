print(123_45)
# getting the BMI from height and weight
weight = float(input('Enter your weight in kgs :'))
height = float(input('Enter your height in cms :'))
bmi = (weight / (height ** 2)) * 10000
bmi=round(bmi, 2) #round upto 2 decimals with nearest whole number
if bmi < 18:
    result = 'Your weight is underweight'
elif 18.5 <= bmi <= 24.9:
    result = 'Your weight is normal'
elif 25 <= bmi <= 29.9:
    result = "You are over weight"
else:
    result = "You are obese"
print(f'Your BMI is {bmi} and {result}')
