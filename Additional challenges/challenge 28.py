'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.
'''
weight = float(input("Enter BMI: "))
if weight < 18.5:
    print("underweight")
elif weight > 18.5 and weight < 25:
    print("normal weight")
elif weight > 25 and weight <30:
    print("slightly overweight")
elif weight > 30 and weight < 35:
    print("obese")
elif weight>35:
    print("clinically obese")
else:
    print("Error")