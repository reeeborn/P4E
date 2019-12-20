fname = input('Enter a file name:')
fhand = open(fname)
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    count = count + 1
    print(words[1])
print('There were %d lines in the files with From as the first word' % count)
