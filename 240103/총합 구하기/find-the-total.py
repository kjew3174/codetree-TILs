data = input().split()
a, b = int(data[0]), int(data[1])
s = 0
for i in range(a, b+1):
    if (i % 6) == 0 and (i % 8) != 0:
        s += i
print(s)