data = input().split()
m, l = int(data[0]), int(data[1])
s = 0
if m >= 90:
    if l >= 95:
        s = 100000
    elif l >= 90:
        s = 50000
print(s)