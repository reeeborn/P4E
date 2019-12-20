def computegrade(score):
    try:
        score=float(s)
    except:
        result='Bad score'
        return result
    if score<0.6:
        result='F'
    elif score<0.7:
        result='D'
    elif score<0.8:
        result='C'
    elif score<0.9:
        result='B'
    elif score<=1:
        result='A'
    else:
        result='Bad score'
    return result
for i in range(4):
    s=input('Enter score:')
    x=computegrade(s)
    print(x)
