str = 'X-DSPAM-Confidence:0.8475'
num = str.find(':')
res = str[num+1:]
f = float(res)
print(f)
