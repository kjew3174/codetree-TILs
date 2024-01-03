n = int(input())
s = 0
for _ in range(n):
    i = int(input())
    s += i
print(f"{s} {s/n:.1f}")