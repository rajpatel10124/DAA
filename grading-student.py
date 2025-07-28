def gradingStudents(grades):
    result = []
    
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            next_multiple = ((grade // 5) + 1) * 5
            if next_multiple - grade < 3:
                result.append(next_multiple)
            else:
                result.append(grade)
    
    return result


# Input
n = int(input())
grades = [int(input()) for _ in range(n)]

rounded_grades = gradingStudents(grades)

# Output
for g in rounded_grades:
    print(g)
