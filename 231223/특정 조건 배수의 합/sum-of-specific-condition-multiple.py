data = input().split()
a, b = int(data[0]), int(data[1])
s = 0
for n in range(a, b+1):
    if (n % 5) == 0:
        s += n
print(s)