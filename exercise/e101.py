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
        dcount[words[1]] = dcount.get(words[1], 0)+1
lsg = sorted([(num, nam) for nam, num in dcount.items()])
x, y = lsg[-1]
print(y, x)
