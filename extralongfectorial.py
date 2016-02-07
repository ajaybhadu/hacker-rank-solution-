import math
import sys

for linenum, testnum in enumerate(sys.stdin):
    if linenum >= 0:
        print math.factorial(int(testnum))
