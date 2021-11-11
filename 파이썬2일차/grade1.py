score = int(input("내 점수는?"))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("학점은 " + grade + " 입니다.")


score = int(input("내 점수는?"))

if score >= 90:
    if score >= 93:
        grade = "A+"
    elif score >= 90:
        grade = "A"
    else:
        grade = "A-"
elif score >= 80:
    if score >= 87:
        grade = "B+"
    elif score >= 85:
        grade = "B"
    else:
        grade = "B-"
elif score >= 70:
    if score >= 80:
        grade = "C+"
    elif score >= 75:
        grade = "C"
    else:
        grade = "C-"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("학점은 " + grade + " 입니다.")
