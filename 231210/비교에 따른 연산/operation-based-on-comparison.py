data = input().split()
a, b = int(data[0]), int(data[1])
if a > b:
    print(a * b)
else:
    print(b // a)