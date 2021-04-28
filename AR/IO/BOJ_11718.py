i = 1
while True:
    try:
        text = input()
        if i <= 100:
            print(text)
            i += 1
    except:
        break
    