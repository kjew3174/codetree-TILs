data = input().split()
a, b, c = int(data[0]), int(data[1]), int(data[2])
lst = a if a <= b else b
lst = c if c <= lst else lst
print(lst)