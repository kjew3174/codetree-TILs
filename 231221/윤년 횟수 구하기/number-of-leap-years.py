count = 0
n = int(input())
for y in range(1, n+1):
    if (y % 100) == 0 and (y % 400) != 0:
        pass
    elif (y % 4) == 0:
        count += 1
    else:
        pass
print(count)