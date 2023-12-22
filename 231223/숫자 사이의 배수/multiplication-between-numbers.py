data = input().split()
a, b = int(data[0]), int(data[1])
s = 0
count = 0
for n in range(a, b+1):
    if (n % 5) == 0 or (n % 7) == 0:
        s += n
        count += 1
print(f"{s} {s/count:.1f}")