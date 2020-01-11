import re
name = input('Enter a file name: ')
fhand = open(name)
count = 0
#lst = []
#nn = 0
for line in fhand:
    #line = line.rstrip()
    #if re.search('[0-9]+',line):
    #    nn = nn + 1
    y = re.findall('[0-9]', line)
    if y == []:
        continue
    else:
        for x in y:
            count = count + int(x)
#for n in lst:
#        print(n)
        #count = count + int(n)
print(count)
#print(count/nn)
