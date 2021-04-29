n = int(input())
for i in range(n, 0, -1):
    blank = int(n - i)
    print(' '*blank+'*'*i)