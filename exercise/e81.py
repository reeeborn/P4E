def chop(t):
    num = len(t)
    t = t[1:num-2]


def middle(t):
    nm = len(t)
    return t[1:nm-2]


x = input('Enter a list:')
print(middle(x))
