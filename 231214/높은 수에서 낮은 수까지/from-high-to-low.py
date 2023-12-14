data = input().split()
a, b = int(data[0]), int(data[1])
if a >= b:
    a, b = b, a
for i in range(b, a-1, -1):
    print(i, end=' ')