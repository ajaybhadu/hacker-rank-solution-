#!/usr/bin/py
 
def manasa(n, a, b):
    solutions = set()
    for i in xrange(n):
        solutions.add(a * i + b * (n-i-1))
 
    return solutions
 
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        n = input()
        a = input()
        b = input()
        l = sorted(list(manasa(n, a, b)))
        print ' '.join(map(str, l))
