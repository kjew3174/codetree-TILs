n = int(input())
for i in range(1, n+1):
    for j in str(i):
        if (int(j) % 3) == 0:
            ans = 0
        elif (i % 3) == 0:
            ans = 0
        else:
            ans = i
    print(ans, end=' ')