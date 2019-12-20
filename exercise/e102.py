fname = input('Please Enter a File Name:')
fhand = open(fname)
dcount = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] != 'From':
        continue
    else:
        str = words[5]
        dt = str.split(':')
        dcount[dt[0]] = dcount.get(dt[0], 0)+1
ls = sorted(dcount.items())
for ds in ls:
    x, y = ds
    print(x, y)
