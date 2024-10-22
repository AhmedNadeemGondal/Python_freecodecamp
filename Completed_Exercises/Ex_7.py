fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    white_space = line.find(' ')
    after_white_space = line[white_space:]
    final_string = after_white_space.strip()
    value = float(final_string)
    #print(value)
    total = total + value
    #print (sum)
    count = count + 1
    average = total/count

print("Average spam confidence:",average)
#print(count)
#mbox-short.txt