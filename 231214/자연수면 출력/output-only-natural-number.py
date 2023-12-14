data = input().split()
a, b = int(data[0]), int(data[1])
if a >= 1:
    for _ in range(b):
        print(a, end='')
else:
    print(0)