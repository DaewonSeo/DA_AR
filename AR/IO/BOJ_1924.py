m, d = map(int, input().split())
months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
days = { 1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT', 0: 'SUN'}
total_days = 0
for n in range(1, m):
    total_days += months[n]
total_days += d
num_to_char = total_days % 7
print(days[num_to_char])