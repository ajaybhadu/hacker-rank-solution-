from math import sqrt, ceil

message = raw_input().strip()

size = len(message)

t1 = int(ceil(sqrt(size)))
t2 = int(ceil(float(size)/t1))

rows = min(t1, t2)
cols = max(t1, t2)

cipher = []

while message:
    cipher.append(message[:cols])
    message = message[cols:]

for j in xrange(cols):
    tmp = []
    for i in xrange(rows):
        try:
            tmp.append(cipher[i][j])
        except IndexError:
            pass
    print ''.join(tmp),
