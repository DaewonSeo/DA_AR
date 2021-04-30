n = int(input())
for i in range(1, n+1):
    if i == 1 or i == n:
        print(' '*(n-i), '*'*(2*i-1), sep='')
    else:
        print(' '*(n-i), '*', ' '*((i-1) * 2 -1), '*', sep='')