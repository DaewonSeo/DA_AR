height = sorted([ int(input()) for _ in range(9)])
total = 100

for h in height:
    if total - h > 0:
        print()
    total += h
    if total <= 100:
        print(h)
        print(total)
