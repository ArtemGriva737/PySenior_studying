import inspect

class Person:
    name: str
    surname: str
    age: int

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def info_person(self):
        print(f'Person:\t{self.name} | {self.surname} | {self.age}')


class Student(Person):
    progress: float
    pensione: bool

    def __init__(self, name: str, surname: str, age: int, progress: float, group=None):
        Person.__init__(self, name, surname, age)
        self.progress = progress
        self.group = group
        self.set_pensione(self.age)

    def set_pensione(self, value: int):
        if value >= 60:
            self.pensione = True
        else:
            self.pensione = False

    def info_student(self):
        print(f'Student: Progress: {self.progress} | Pension: {self.pensione}')

    def info_all(self):
        self.info_person()
        self.info_student()
        self.group.info_group()


class Worker(Person):
    position: str
    duties: list
    pensione: bool

    def __init__(self, name: str, surname: str, age: int, position: str, duties: list):
        Person.__init__(self, name, surname, age)
        self.position = position
        self.duties = duties
        self.set_pensione(self.age)

    def set_pensione(self, value: int):
        if value >= 60:
            self.pensione = True
        else:
            self.pensione = False

    def info_worker(self):
        print(f'Worker:\tPosition: {self.position} | Duties: {", ".join(self.duties)} | Pension: {self.pensione}')

    def info_all(self):
        self.info_person()
        self.info_worker()


class Group:
    name: str
    age_category: int
    students: list
    workers: list

    def __init__(self, name: str, age_category: int, students: list, workers: list):
        self.name = name
        self.age_category = age_category
        self.students = students
        self.workers = workers

    def info_group(self):
        print(f'Group: {self.name} | Students: {len(self.students)} | Age category: {self.age_category}')

    def info_all(self):
        print('\n')
        for student in self.students:
            student.info_all()
        print('\n')
        for worker in self.workers:
            worker.info_all()


student = Student(name='Ivan', surname='Shevchenko', age=19, progress=4.5)
worker = Worker(name='Sergey', surname='Leonenko', age=35, position='Policeman', duties=['Follow the order', 'Catch criminals'])
group = Group(name='Group A', age_category=18, students=[student], workers=[worker])
student.group = group

group.info_all()


def get_attributes(cls):
    return [name for name, value in inspect.getmembers(cls, lambda a: not inspect.isfunction(a) or inspect.ismethod(a))
            if not name.startswith('__')]

def get_methods(cls):
    return [name for name, value in inspect.getmembers(cls, inspect.isfunction or inspect.ismethod)
            if not name.startswith('__')]

classes = [Student, Worker]

for cls in classes:
    print(f"\n=== {cls.__name__} ===")
    print("Атрибути:", get_attributes(cls))
    print("Методи:", get_methods(cls))


