data = input().split()
h, m = int(data[0]), int(data[1])
bmi = int(m*10000 / h**2)
print(bmi)
if bmi >= 25:
    print("Obesity")