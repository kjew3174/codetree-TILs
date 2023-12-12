a = 0

for i in range(3):
    data = input().split()
    stm, tmp = str(data[0]), float(data[1])
    if stm == 'Y' and tmp >= 37:
        a += 1

if a >= 2:
    ans = 'E'
else:
    ans = 'N'
print(ans)