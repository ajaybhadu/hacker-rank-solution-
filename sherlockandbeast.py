T = int(input())
for i in range(T):
    k = int(input())
    n5 = k
    n3 = 0
    done = False
    while n5 >= 0:
        if n5%3 == 0 and n3%5 == 0:
            for j in range(n5):
                print('5',end='')
            for j in range(n3):
                print('3',end='')
            print()
            done = True
            break
        n5 -= 1
        n3 += 1
    if not done:
        print(-1)
