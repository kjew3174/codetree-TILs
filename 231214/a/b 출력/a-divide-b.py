data = input().split()
a, b = int(data[0]), int(data[1])
digit = 0
r = a
ans = ''
while digit <= 20:
    q = r // b
    r = r - q*b
    r *= 10
    ans += str(q)
    if digit == 0:
        ans += '.'
    
    digit += 1
print(ans)