
N = 2 ** 11
uniqProb = 1.0
n = 0

while 1 - uniqProb < 0.75:
    n += 1
    uniqProb *= (N - n)/N

print(n)