def computepay(h, r):
    hours = h
    rate_per_hour = r
    try: 
        hours = float(hours)
        rate_per_hour =float(rate_per_hour)
    except:
        return("Non numeric input")
        exit()
    if hours > 40:
        #print ('Ovetime')
        pay = (40 * rate_per_hour) + ((hours-40)* (1.5 * rate_per_hour))
        return pay
    else:
        #print ('Regular')
        pay = (hours * rate_per_hour) 
        return pay

h = input("work hours:")
r = input ("rate:")

output = computepay(h, r)
print("Pay",output)