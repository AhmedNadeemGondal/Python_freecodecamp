
handle = open("mbox-short.txt")
counts = dict()
lst_t = list()
for i in handle:
    if not i.startswith("From "):
        continue
    lst = i.split()
    b = lst[5]
    a = b.split(':')
    lst_t.append(a[0])


for time in lst_t:
    counts[time] = counts.get(time,0) + 1

lst = list()
for k,v in counts.items():
    ntuple = (k,v)
    lst.append(ntuple)

lst = sorted(lst)

for i in range(len(lst)):
    a = lst[i]
    print(a[0],a[1])