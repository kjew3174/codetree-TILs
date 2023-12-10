data = input().split()
h, m = int(data[0])*100, int(data[1])
bmi = int(m / h**2)
print(bmi)
if bmi >= 25:
    print("Obesity")