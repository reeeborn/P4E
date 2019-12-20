fname = input('Enter a file name:')
fhand = open(fname)
count = 0
f = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence'):
        num = line.find(':')
        res = line[num+1:]
        count = count+float(res)
        f = f+1
print(count/f)
