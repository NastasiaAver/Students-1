grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
num_students = len(students)
print("Кол-во студентов:",len(students))
print('Кол-во оценок:', len(grades))
print('Совпадает ли кол-во студентов и оценок:', len(grades) == len(students))
students = sorted(students)
grade_1 = sum(grades[0])/len(grades[0])
grade_2 = sum(grades[1])/len(grades[1])
grade_3 = sum(grades[2])/len(grades[2])
grade_4 = sum(grades[3])/len(grades[3])
grade_5 = sum(grades[4])/len(grades[4])
grades = [[grade_1], [grade_2], [grade_3], [grade_4], [grade_5]]
result = {students[n]: grades[n] for n in range(len(students))}
print("Средний балл:", result)