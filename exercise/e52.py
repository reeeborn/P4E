i = 5
Bnum = None
Snum = None
cnt = 0
tol = 0
while i != 0:
    No = input('Enter a number:')
    if No == 'done':
        break
    else:
        try:
            num = float(No)
            tol = tol + num
            cnt = cnt+1
            if Bnum is None or Bnum < num:
                Bnum = num
            if Snum is None or Snum > num:
                Snum = num
        except:
            print('Invalid input')
            continue
print(tol, cnt, Bnum, Snum)
