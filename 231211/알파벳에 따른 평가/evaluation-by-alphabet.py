grade = str(input())
if grade == 'S':
    msg = "Superior"
elif grade == 'A':
    msg = "Excellent"
elif grade == 'B':
    msg = "Good"
elif grade == 'C':
    msg = "Usually"
elif grade == 'D':
    msg = "Effort"
else:
    msg = "Failure"
print(msg)