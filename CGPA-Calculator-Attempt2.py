import csv
grade_points = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}
csv_file = open("CGPA.csv", "r")
# writeCSV = csv.DictReader(cgpafile, delimiter=",")
# with open("CGPA.csv", "r") as csv_file:
csv_reader = csv.reader(csv_file)
next(csv_reader)


def total_score(gradepoint, units):
    return gradepoint / units


course_units = []
attained_grades = []

for line in csv_reader:
    course_unit = int(line[1])
    course_units.append(course_unit)

    attained_grade = line[3].strip()
    attained_grades.append(grade_points[attained_grade] * course_unit)

print(total_score(sum(attained_grades), sum(course_units)))
csv_file.close()