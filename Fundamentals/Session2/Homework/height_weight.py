height_cm = float(input("height ? "))
weight = float(input("weight ? "))
height = height_cm / 100
BMI = weight / (height * height)
print("BMI = ",BMI)
if BMI < 16 :
    print("Severely underweight")
elif BMI < 18.5 :
    print("Underweight")
elif BMI < 25 :
    print("Normal")
elif BMI <30 :
    print("Overweight")
else :
   print("Obese")