score = float (input("Enter Score: "))
#score = float(score)
if 1 < score or score < 0:
    print ("error")
elif 1 > score >= 0.9:
    print ("A")
elif 0.9 > score >= 0.8:
    print ("B")
elif 0.8 > score >= 0.7:
    print ("C")
elif 0.7 > score >= 0.6:
    print ("D")
else:
    print ("F")