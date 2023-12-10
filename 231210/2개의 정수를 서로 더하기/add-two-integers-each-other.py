data = input().split()
a, b = int(data[0]), int(data[1])
a += b
b += a
print(a, b)