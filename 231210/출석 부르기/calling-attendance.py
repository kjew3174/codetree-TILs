attend = ["John", "Tom", "Paul"]
n = int(input())
if n > len(attend) or n <= 0:
    print("Vacancy")
else:
    n -= 1
    print(attend[n])