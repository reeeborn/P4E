H=input('Enter Hours:')
hour=float(H)
R=input('Enter Rate:')
rate=float(R);
if hour<=40:
    pay=hour*rate
else:
    pay=hour*rate*1.5
print(pay)
