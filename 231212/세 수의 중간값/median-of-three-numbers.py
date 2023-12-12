data = input().split()
a, b, c = int(data[0]), int(data[1]), int(data[2])
ans = 1 if b > a and b < c else 0
print(ans)