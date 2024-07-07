grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(students)

def calculate_average_grade(student_grades):
    return sum(student_grades) / len(student_grades)

def calculate_student_averages(grades, students):
    student_averages = {}

    for student, grade_list in zip(students, grades):
        student_averages[student] = calculate_average_grade(grade_list)

    return student_averages

student_averages = calculate_student_averages(grades, students_list)
print(student_averages)