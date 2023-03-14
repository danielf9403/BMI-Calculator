weight = float(input())
height = float(input())
xheight = height**2
print(xheight)
x = weight//xheight

bmi = x
while bmi == x :
  bmi+= 1
  if bmi <= 18.5:
    print("Underweight", +bmi)
if bmi > 18.6 and bmi <=25:
    print("Normal")
if bmi >25 and bmi <= 30:
    print("Overweight", +bmi)
if bmi > 30:
    print("Obesity", +bmi)