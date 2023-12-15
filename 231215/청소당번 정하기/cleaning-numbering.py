n = int(input())
c = 0; h = 0; t = 0;
for date in range(n+1):
    if date == 0:
        pass
    elif (date % 12) == 0:
        t += 1
    elif (date % 3) == 0:
        h += 1
    elif (date % 2) == 0:
        c += 1
    else:
        pass
print(c, h, t)