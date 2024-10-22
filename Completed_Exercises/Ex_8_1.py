fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for x in fh:
    wrds = x.split()

    for i in wrds:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)