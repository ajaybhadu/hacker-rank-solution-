#!/usr/bin/env python

import collections, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    a = sorted(map(int, sys.stdin.readline().split()))
    
    c = collections.Counter(a)
    count = [c[k] for k in sorted(c)]
    
    for i in range(len(count)):
    	print(sum(count[i:]))
