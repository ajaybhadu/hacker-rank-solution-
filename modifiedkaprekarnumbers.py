import math

def is_kap(n):
    n_sqr = int(math.pow(n, 2))
    str_n_sqr = str(n_sqr)
    if len(str_n_sqr) == 1:
        l = 0
        r = n_sqr
    else:
        l = int(str_n_sqr[0:math.floor(len(str_n_sqr) / 2)])
        r = int(str_n_sqr[math.floor(len(str_n_sqr) / 2):len(str_n_sqr)])
    return n == l + r

p = int(input())
q = int(input())
x = []
for i in range(p, q + 1):
    if is_kap(i):
        x.append(i)
if len(x) == 0:
    print("INVALID RANGE")
else:
    x = list(map(str, x))
    print(" ".join(x))
