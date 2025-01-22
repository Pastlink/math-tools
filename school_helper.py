from common_tools import cprint, colorize, is_int

class Student:
    def __init__(self, name: str, age: int, grade: int) -> None:
        self.name = name.title()
        self.age = age
        self.grade = grade # 0 - 100

    def __repr__(self) -> str:
        return repr((self.name, self.age, self.grade))

    def get_grade(self):
        return self.grade

    def add_to_grade(self, value_to_add: int):
        self.grade += value_to_add

    def set_grade(self, new_grade: int):
        self.grade = new_grade

class Course:
    def __init__(self, course_name: str, max_students: int):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []

    def __repr__(self) -> str:
        return repr((self.course_name, self.max_students))

    def add_student(self, student: Student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        value = is_int(value / len(self.students), 2)

        return grade_judge(value)

    def print_course_takers(self) -> None:
        students_enrolled = len(self.students)
        if students_enrolled < 1:
            return None

        cprint(f"{self.course_name} Class", "Green")
        lst_students = sorted(self.students, key=lambda student: student.name)
        for i in range(students_enrolled):
            print(f"{i+1}. {lst_students[i].name} - {lst_students[i].grade}")

class Group:
    def __init__(self, group: str, turn: str) -> None:
        self.group = group.title()
        self.turn = turn.title()
        self.classes = []

    def __repr__(self) -> str:
        return repr((self.group, self.turn))

    def get_classes(self):
        return self.classes

    def add_class(self, course: Course):
        self.classes.append(course)

def grade_judge(value) -> str:
    if value < 50:
        value = colorize(value, "Red")
    elif value < 70:
        value = colorize(value, "Yellow")
    else:
        value = colorize(value, "Green")

    return value

def print_all_groups(groups: list) -> None:
    for i in groups:
        print(f"Group: {colorize(i.group, "Green")} Turn: {colorize(i.turn, "Green")}")
        for j in range(len(i.classes)):
            i.classes[j].print_course_takers()
            cprint(f"{i.classes[j].course_name} Class average: {i.classes[j].get_average_grade()}", "Blue")

# Science, English, Math, French, Psychology

group1A = Group("1-A", "Morning")
group1B = Group("1-B", "Morning")
group1C = Group("1-C", "Afternoon")

groups = [group1A, group1B, group1C]

s1 = Student("Tim", 19, 85)
s2 = Student("Bill", 19, 65)
s3 = Student("Jill", 19, 55)

group1A.add_class(Course("Science", 2))
group1A.add_class(Course("Psychology", 3))
group1B.add_class(Course("Math", 2))
group1C.add_class(Course("French", 2))

sci_class = group1A.classes[0]
sci_class.add_student(s1)
sci_class.add_student(s2)

psy_class = group1A.classes[1]
psy_class.add_student(s1)
psy_class.add_student(s2)
psy_class.add_student(s3)

math_class = group1B.classes[0]
math_class.add_student(s1)
math_class.add_student(s2)
math_class.add_student(s3)

french_class = group1C.classes[0]
french_class.add_student(s1)
french_class.add_student(s3)

print_all_groups(groups)
