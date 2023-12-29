s = 0
count = 0
for _ in range(10):
    n = int(input())
    if n >= 0 and n <= 200:
        s += n
        count += 1
print(f"{s} {s/count:.1f}")