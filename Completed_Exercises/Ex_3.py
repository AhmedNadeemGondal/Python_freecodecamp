hours = input("work hours:")
rate_per_hour = input ("rate:")
hours = float(hours)
rate_per_hour =float(rate_per_hour)
if hours > 40:
    print ('Ovetime')
    pay = (40 * rate_per_hour) + ((hours-40)* (1.5 * rate_per_hour))
    print ("Pay:",pay)
else:
    print ('Regular')
    pay = (hours * rate_per_hour)
    print ("Pay:",pay)
