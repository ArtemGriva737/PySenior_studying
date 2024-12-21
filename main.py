class StudySubject:
    name: str
    hours: int
    enable: bool

    def __init__(self):
        self.name = str(input('Введіть назву предмету: '))
        self.hours = int(input('Введіть кількість годин потрібну для вивчення предмета: '))
        self.enable = bool(input('Введіть чи вивчається зараз цей предмет (1 - так, 0 - ні): '))

    def info_study(self):
        print(f'Study: {self.name} | {self.hours} | {"Активен" if self.enable else "Не активен"}')


class Student:
    name: str
    surname: str
    subjects: list

    def __init__(self):
        self.name = str(input('Введіть імя студента: '))
        self.surname = str(input('Введіть прізвище студента: '))
        self.subjects = []
        num_subjects = int(input('Введіть кількість предметів для студента: '))
        for _ in range(num_subjects):
            subject = StudySubject()
            self.subjects.append(subject)

    def info_student(self):
        print(f'Student: {self.name} | {self.surname}')

    def info_all(self):
        self.info_student()
        for subject in self.subjects:
            subject.info_study()


class Group:
    name: str
    age_category: int
    students: list

    def __init__(self):
        self.name = str(input('Введіть назву групи: '))
        self.age_category = int(input('Введіть вікову категорію (від скількох років): '))
        self.students = []
        num_students = int(input('Введіть кількість студентів у групі: '))
        for _ in range(num_students):
            student = Student()
            self.students.append(student)

    def info_group(self):
        print(f'Group: {self.name} | Students: {len(self.students)} | Age category: {self.age_category}')

    def info_all(self):
        self.info_group()
        for student in self.students:
            student.info_all()


group = Group()
group.info_all()