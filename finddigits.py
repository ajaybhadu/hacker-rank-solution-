def func(A):
    return len([1 for i in str(A) if i !='0' and A%int(i)==0])

for t in range(int(input())):
    print(func(int(input())))
