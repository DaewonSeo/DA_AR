numbers = input().split(' ')
print(' '.join(sorted(numbers, key=lambda x: int(x))))


# unpacking 활용
# print(*sorted(list(map(int, input.split()))))