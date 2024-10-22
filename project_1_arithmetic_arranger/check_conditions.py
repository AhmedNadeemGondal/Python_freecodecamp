

inp1 = ["1244 + 6983", "3801 - 2", "55 + 43", "1234 + 4944"]

if len(inp1) > 5:
    print('Error: Too many problems.')

for i in inp1:
    if any(j.isalpha() for j in i) == True:
          print ('Error: Numbers must only contain digits.')
    if i.find('/') != -1 or i.find('*') != -1:
         print ("Error: Operator must be '+' or '-'.")
    div = i.split()
    # if (k.isdigit() 
    
    # if any(len(k)>3 for k in div ):
    #     print ("Error: Numbers cannot be more than four digits.", div)
    flag = False
    for k in div:
        # print(k)
        if len(k)>4:
            flag = True
            print ("Error: Numbers cannot be more than four digits.")
            break
    if flag:
         break   
    print('np') 

         




# for i in inp_array:
#     if re.search('[a-zA-Z]',i):
#         
#         break
#     if re.search('r"[/*]"',i):
#         print ('Error: Operator must be '+' or '-'.')
#         break        
    # seperated = i.split()
    # for i in seperated:
    #     if i == '+' or i == '-':
