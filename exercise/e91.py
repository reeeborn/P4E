fhand = open('words.txt')
n = 0
em = dict()
for line in fhand:
    words = line.split()
    for word in words:
        em[word] = n
        n = n+1
fword = input('Please Enter a Word:')
flag1 = fword in em
print(flag1)
