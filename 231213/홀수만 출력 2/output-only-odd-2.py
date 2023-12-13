data = input().split()
a, b = int(data[0]), int(data[1])
for i in range(a, b-1, -2):
    print(i, end=' ')