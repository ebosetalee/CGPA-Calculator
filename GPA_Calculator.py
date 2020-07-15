courses = int(input("How many courses except GST did you do? "))
total_unit = int(input("What is the total Units of the courses? "))
count = 0
A = 5
B = 4
C = 3
D = 2
E = 1
F = 0
grade_score = 0
while count < courses:
    new_courses = input("What is the name of the course? ")
    unit = int(input("What is the unit of this course: "))
    score = int(input("What did you score? ")) 
    if score >= 70 and score <= 100:
        score = A
        print("You had A in {}.".format(new_courses))
    elif (score < 70) and (score >= 60):
        score = B
        print("You had B in {}.".format(new_courses))
    elif score >= 50 and score < 60:
        score = C
        print("You had C in {}.".format(new_courses))
    elif score >= 45 and score < 50:
        score = D
        print("You had D in {}.".format(new_courses))
    elif score < 45 and score >= 40:
        score = E
        print("You had E in {}.".format(new_courses))
    else:
        score = F
        print("You had F in {}.".format(new_courses))
    new_score = (score * unit) + grade_score 
    print(new_score)
    grade_score = new_score
    count += 1
total_score = new_score
print(total_score)
total_score = 56
def gpa(grade = total_score):
    results = total_score / total_unit
    print(results)
gpa()