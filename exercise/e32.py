H=input('Enter Hours:')
try:
    hour=float(H)
except:
    print('please enther numeric input')
    exit()
R=input('Enter Rate:')
try:
    rate=float(R)
except:
    print('please enther numeric input')
    exit()
pay=rate*hour
print(pay)
