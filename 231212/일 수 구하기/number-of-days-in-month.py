n = int(input())
if n != 2:
    if n <= 7:
        if (n % 2) == 0:
            date = 30
        else:
            date = 31
    else:
        if (n % 2) == 0:
            date = 31
        else:
            date = 30
else:
    date = 28
print(date)