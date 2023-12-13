data = input().split()
b, a = int(data[0]), int(data[1])
count = b
while count >= a:
    if (count % 2) == 0:
        print(count, end=' ')
    count -= 1