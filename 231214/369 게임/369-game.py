n = int(input())
for i in range(1, n+1):
    data = str(i).split('')
    for j in data:
        if (j % 3) == 0 or (i % 3) == 0:
            print(0, end=' ')
        else:
            print(i, end=' ')