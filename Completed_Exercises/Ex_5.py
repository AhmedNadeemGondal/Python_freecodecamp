largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = float(num)
    except:
        print ('Invalid input')
    if isinstance(num, float) == True:
        if largest is None:
            largest = num
            smallest = num
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
largest = int(largest)
smallest = int(smallest)
print("Maximum is", largest)
print("Minimum is", smallest)