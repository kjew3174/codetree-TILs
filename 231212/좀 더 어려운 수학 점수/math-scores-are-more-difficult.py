data = input().split()
am, ae = int(data[0]), int(data[1])
data = input().split()
bm, be = int(data[0]), int(data[1])

if am != bm:
    ans = ('A' if am > bm else 'B')
else:
    ans = ('A' if ae > be else 'B')
print(ans)