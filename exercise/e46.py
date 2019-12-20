def computepay(hour,rate):
    H=float(hour)
    R=float(rate)
    if H<=40:
        pay=H*R
    else:
        pay=H*R*1.5
        print('Pay:',pay)
x=input('Enter hours:')
y=input('Enter Rate:')
computepay(x,y)
