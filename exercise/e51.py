num = 0
tol = 0
count = 0
while True:
    No = input('Enter a number:')
    if No == 'done':
        break
    else:
        try:
            num = float(No)
            tol = tol+num
            count = count+1
        except:
            print('Invalid input')
            continue
print(tol, count, tol/count)
