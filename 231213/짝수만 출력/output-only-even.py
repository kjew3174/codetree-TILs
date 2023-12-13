data = input().split()
a, b = int(data[0]), int(data[1])
count = a
while count <= b:
    if (count % 2) == 0:
        print(count, end=' ')
    else:
        pass
    count += 1