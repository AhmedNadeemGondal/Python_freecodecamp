

inp1 = ["1244 + 6983", "3801 - 2", "55 + 43", "1234 + 4944"]

line1 = ""
line2 = ""
line3 = ""
line4 = ""


for i in inp1:
    div = i.split()
    if len(div[0]) > len(div[1]):
        length = len(div[0]) + 2
    elif len(div[0]) < len(div[1]):
        length = len(div[1]) + 2
    else:
        length = len(div[0]) + 2


    for i in range(length - len(div[0])):
        line1 += line1.join(' ')
    line1 += div[0] + '    '

    for i in range(length - len(div[2])):
        if i == 0:
            line2 += div[1]
        else:
            line2 += line2.join(' ')
    line2 += div[2] + '    '
    for i in range(length):
        line3 += line1.join('-')
    line3 += "    "
    add_ans = int(div[0]) + int(div[2])
    for i in range(length -len(str(add_ans))):
        line4 += line4.join(' ')
    line4 += str(add_ans)
    line4 += "    "


print(line1+ '\n' + line2 + '\n' + line3+ '\n' + line4)
# print(line2)
# print(line3)
# print(line4)

    # line1 += line1.join(div[0])
    # print(line1)