data = input().split()
a, b = int(data[0]), int(data[1])
for i in range(b, a-1, -1):
    print(i, end=' ')