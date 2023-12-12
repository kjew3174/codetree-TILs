data = input().split()
a, b, c = int(data[0]), int(data[1]), int(data[2])
if a <= b:
    lst = a
else:
    lst = b
if c <= lst:
    lst = c
ans1 = 1 if a == lst else 0
ans2 = 1 if a == b and b == c else 0
print(ans1, ans2)