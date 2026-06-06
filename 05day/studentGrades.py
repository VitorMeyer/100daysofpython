studentGrades = [
  8.5, 7.2, 9.0, 6.5, 10.0, 
  5.5, 8.0, 7.8, 9.5, 6.0,
  7.5, 8.8, 9.2, 5.0, 6.8, 
  7.0, 8.2, 9.8, 6.2, 7.4,
  8.6, 9.4, 5.8, 6.6, 7.6, 
  8.4, 9.6, 6.4, 7.9, 8.9
    ]

sum_student_grades = sum(studentGrades)
print(f"{sum_student_grades:.2f}")

sum_manual = 0

for studentGrade in studentGrades:
    sum_manual += studentGrade

print(f"{sum_manual:.2f}")

print(max(studentGrades))

maxGrade = 0

for score in studentGrades:
    if score > maxGrade:
        maxGrade = score
        print(maxGrade)
print(maxGrade)
