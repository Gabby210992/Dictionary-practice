print("Welcome to my dictionary grading program")
students_scores ={"James": 70, "Joy":90, "Comfort":60}

student_grade ={}
for key in students_scores:
    if students_scores[key] >= 90:
        students_scores[key] = "Outstanding"
    elif students_scores[key] >= 80:
        students_scores[key] = "Great"

    elif students_scores[key] >= 70:
        students_scores[key] = "Good job"

    else:
        students_scores[key] = "You failed"

    student_grade[key] = students_scores[key]

print(student_grade)