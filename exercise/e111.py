import re
fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
word = input('Enter a regular expression: ')
for line in fhand:
    line = line.rstrip()
    if re.search(word, line):
        count = count+1
print('%s had %d lines that matched %s' % (fname, count, word))
