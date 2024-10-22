list1 = [3, 9,9, 4, 7, 7, 1, 2]
list2 = [3, 6, 9, 1, 4, 7, 7]
condition = True
for value in list1:
    if list2.count(value) < list1.count(value): 
        print(f"{value} is not present enough times in list2")
        condition = False
        break
else:
    print("All items in list1 are present in list2 with the required frequency")

print(f'Condition is {condition}')
