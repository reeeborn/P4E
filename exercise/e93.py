fname = input('Please Enter a File Name:')
fhand = open(fname)
dcount = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    #print(words)
    if len(words) == 0:
        continue
    if words[0] != 'From':
        continue
    else:
        dcount[words[1]] = dcount.get(words[1], 0)+1
print(dcount)
