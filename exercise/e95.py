fname = input('Please Enter a File Name:')
fhand = open(fname)
dcount = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] != 'From:':
        continue
    else:
        t = words[1].find('@')
        str = words[1]
        tstr = str[t+1:]
        dcount[tstr] = dcount.get(tstr, 0)+1
print(dcount)
