import re
handle = open("regex_sum_1711777.txt")
numbers = list()
for i in handle:
    ints = re.findall('([0-9]+)',i)
    if len(ints) == 0: continue
    for j in range(len(ints)):
        numbers.append(ints[j])

res = [eval(i) for i in numbers]
sum = sum(res)
print (sum)
