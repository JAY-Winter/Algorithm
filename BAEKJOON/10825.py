N = int(input())

students = {}

for _ in range(N):
    이름, 국어, 영어, 수학 = input().split()
    국어 = int(국어)
    영어 = int(영어)
    수학 = int(수학)


    students[이름] = [국어, 영어, 수학]

# print(students)

sorted_students = sorted(students.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0]))
# sorted_students = sorted(students.items(), lambda item: item[0])
for student in sorted_students:
    print(student[0])