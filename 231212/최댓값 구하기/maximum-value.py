data = input().split()
a, b, c = int(data[0]), int(data[1]), int(data[2])
bst = a if a >= b else b
bst = c if c >= bst else bst
print(bst)