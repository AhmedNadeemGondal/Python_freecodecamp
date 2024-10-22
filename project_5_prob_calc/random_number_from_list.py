import random

hat1 = ['yellow', 'yellow', 'yellow', 'blue', 'blue', 'green', 'green', 'green', 'green', 'green', 'green', 'red', 'red']
draw_count = 2

random.seed(95)
contents = []
for values in range(draw_count):
    print(values)
    r_num = random.randint(0,len(hat1))
    contents.append(hat1.pop(r_num))

    print(r_num, len(hat1))
print(contents)
print(hat1)