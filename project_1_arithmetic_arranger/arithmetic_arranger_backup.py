def arithmetic_arranger(inp1,sum=False):
    if len(inp1) > 5:
        return('Error: Too many problems.')

    for i in inp1:
        if any(j.isalpha() for j in i) == True:
            return ('Error: Numbers must only contain digits.')
        if i.find('/') != -1 or i.find('*') != -1:
            return ("Error: Operator must be '+' or '-'.")
        div = i.split()
        for k in div:
            if len(k)>4:
                return ("Error: Numbers cannot be more than four digits.")

    
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""


    for i in inp1:
        div = i.split()
        if len(div[0]) > len(div[2]):
            length = len(div[0]) + 2
        elif len(div[0]) < len(div[2]):
            length = len(div[2]) + 2
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
        

        if sum == True:
            if div[1] == '+':
                add_ans = int(div[0]) + int(div[2])
            else:
                add_ans = int(div[0]) - int(div[2])
            for i in range(length -len(str(add_ans))):
                line4 += line4.join(' ')
            line4 += str(add_ans)
            line4 += "    "
    if sum == False:
        return(line1+ '\n' + line2 + '\n' + line3)
    else:
        return(line1 + '\n' + line2 + '\n' + line3 + '\n' + line4)


print(arithmetic_arranger(['3801 - 2', '123 + 49']))