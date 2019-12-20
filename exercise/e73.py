fname = input('Enter a file name:')
try:
    fhand = open(fname)
except:
    if fname=='na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print('File cannot be opened:',fname)
    exit()
ln = len(fhand.read())
print('There were %d lines in %s'%(ln,fname))
