y = int(input())
if (y % 4) == 0:
    if (y % 100) == 0:
        if (y % 400) == 0:
            ans = "true"
        else:
            ans = "false"
    else:
        ans = "true"
else:
    ans = "false"
print(ans)