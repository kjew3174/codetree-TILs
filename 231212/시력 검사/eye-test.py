a = float(input())
b = float(input())
if a >= 1 and b >= 1:
    msg = "High"
elif a >= 0.5 and b >= 0.5:
    msg = "Middle"
else:
    msg = "Low"
print(msg)