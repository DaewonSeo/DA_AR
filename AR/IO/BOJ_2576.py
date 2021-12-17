numbers = [input() for _ in range(7)]
odds = sorted([ int(num) for num in numbers if int(num) % 2 != 0 ])

if len(odds) == 0:
    print(-1)
else:
    print(sum(odds), odds[0], sep='\n') 