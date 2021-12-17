line1 = sum(list(map(int, input().split())))
line2 = sum(list(map(int, input().split())))
line3 = sum(list(map(int, input().split())))

total_list = [line1, line2, line3]
for numbers in total_list:
    if numbers == 4:
        print("E")
    elif numbers == 3:
        print("A")
    elif numbers == 2:
        print("B")
    elif numbers == 1:
        print("C")
    else:
        print("D")
