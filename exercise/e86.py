list = []
while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    try:
        nm = float(x)
    except:
        continue
    list.append(nm)
print('Maximum: %0.1f' % max(list))
print('Minimum: %0.1f' % min(list))
