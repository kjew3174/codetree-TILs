data = input().split()
a, b, c = int(data[0]), int(data[1]), int(data[2])
if a > b:
    if a > c:
        if b > c:
            ans = b
        else:
            ans = c
    else:
        ans = a
else:
    if b > c:
        if a > c:
            ans = a
        else:
            ans = c
    else:
        ans = b

print(ans)