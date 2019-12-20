import string
fname = input('Please Enter a File Name:')
fhand = open(fname)
dcount = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.translate(line.maketrans('', '', string.digits))
    line = line.translate(line.maketrans('', '', string.whitespace))
    line = line.lower()
    for letter in line:
        dcount[letter] = dcount.get(letter, 0)+1
ls = sorted([(num, word) for word, num in dcount.items()], reverse=True)
t = len(ls)
for x in range(t):
    y, z = ls[x]
    print(z, y)
