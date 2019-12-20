fname = input('Enter a file name:')
try:
    fhand = open(fname)
except:
    print('Wrong file name!')
    exit()
for line in fhand:
    line1 = line.rstrip().upper()
    print(line1)
