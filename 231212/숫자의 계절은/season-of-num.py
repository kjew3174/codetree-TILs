m = int(input())
if m < 3:
    s = "Winter"
elif m < 6:
    s = "Spring"
elif m < 9:
    s = "Summer"
elif m < 12:
    s = "Fall"
else:
    s = "Winter"

print(s)