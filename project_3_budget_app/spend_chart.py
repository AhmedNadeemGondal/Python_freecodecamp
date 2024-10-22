data = [60, 20, 10]
names = ['Food', 'Clothing', 'Auto']

for i in range(100,-10,-10):
    print("{:>3}|".format(i), end="")
    for j in data:
        if j >= i:
            print(' o ', end="")
        else:
            print('   ', end="")
    print()
len_dash = 3*len(data)+1
print('    ', end='')
for i in range(len_dash):
    print('-',end='')
print()

for i in range(len(max(names, key=len))):
    print('     ', end='')
    for name in names:
        if i < len(name):
            print(name[i], end="  ")
        else:
            print("   ", end="")
    print()