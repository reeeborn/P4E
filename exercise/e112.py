import re
name = input('Enter a file name: ')
fhand = open(name)
count = 0
#lst = []
nn = 0
for line in fhand:
    line = line.rstrip()
    # 也可以'^N.*: ([0-9]+)'
    if re.search('^New Revision:\s+([0-9]+)',line):
        nn = nn + 1
    y = re.findall('^New Revision:\s+([0-9]+)', line)
    if y == []:
        continue
    else:
        for x in y:
            count = count + int(x)
#for n in lst:
#        print(n)
        #count = count + int(n)
print(int(count/nn))
