g = int(input())
a = int(input())
if g == 0:
    if a >= 19:
        msg = "MAN"
    else:
        msg = "BOY"
else:
    if a >= 10:
        msg = "WOMAN"
    else:
        msg = "GIRL"
print(msg)