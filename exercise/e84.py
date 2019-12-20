fname = input('Enter file:')
fhand = open(fname)
list = []
for line in fhand:
    words = line.split()
    for i in words:
        if i in list: continue
        list.append(i)
list.sort()
print(list)
