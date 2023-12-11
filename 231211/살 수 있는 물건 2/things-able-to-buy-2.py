n = int(input())
if n >= 3000:
    item = "book"
elif n >= 1000:
    item = "mask"
elif n >= 500:
    item = "pen"
else:
    item = "no"
print(item)