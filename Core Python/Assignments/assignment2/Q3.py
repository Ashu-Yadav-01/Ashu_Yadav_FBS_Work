#Q3Convert distance given in feet and inches into meter and centimeter
#1 Foot = 0.3048 Meter
#1 Inch = 2.54 Centimeter

feet = int(input('Enter Feet: '))
inches = int(input('Enter Inches: '))


#meter = feet * 0.3048
#centimeter = inches * 2.54

#print('Meter: ', meter)
#print('Centimeter: ', centimeter)
total_inches = (feet * 12) + inches

total_cm = total_inches * 2.54
total_m = total_cm / 100

print("Distance in Meter =", total_m)
print("Distance in Centimeter =", total_cm)

