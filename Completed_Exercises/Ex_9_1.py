handle = open("mbox-short.txt")
counts = dict()
lst_1 = list()
for i in handle:
    if not i.startswith("From "):
        continue
    lst = i.split()
    lst_1.append(lst[1])
for address in lst_1:
    counts[address] = counts.get(address,0) + 1
# print (len(lst_1))
# print(counts)

bcount = None
bword = None
for word,count in counts.items():
    if bcount is None or count > bcount:
        bword = word
        bcount = count
print(bword,bcount)