
handle = open("mbox-short.txt")
counts = dict()
lst_1 = list()
lst_t = list()

for i in handle:
    if not i.startswith("From "):
        continue
    lst = i.split()
    lst_1.append(lst[5])

for i in lst_1:
    lst = i.split(':')
    lst_t.append(lst[0])

for time in lst_t:
    counts[time] = counts.get(time,0) + 1
lst = list()
for k,v in counts.items():
    ntuple = (k,v)
    lst.append(ntuple)

lst = sorted(lst)

for i in range(len(lst)):
    print(lst[i])

