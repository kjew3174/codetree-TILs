data = input().split()
a, b = int(data[0]), int(data[1])
while a < b:
    print(a, end=' ')
    if (a % 2) == 0:
        a += 3
    else:
        a *= 2