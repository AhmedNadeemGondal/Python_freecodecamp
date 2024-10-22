fname = input("Enter file name: ")
fh = open(fname)
lst = list()
count = 0
for x in fh:
    if not x.startswith("From "):
        continue
    wrds = x.split()
    len(wrds)
    print(wrds[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")