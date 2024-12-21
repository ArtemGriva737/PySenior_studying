import random


class Student:
    def __init__(self, name, money=1000, grades=75, energy=100):
        self.name = name
        self.money = money
        self.grades = grades
        self.energy = energy
        self.turn_counter = 0

    def work(self):
        if self.energy > 70:
            earned_money = random.randint(15000, 30000)
            self.money += earned_money
            self.energy -= 10
            print(f"{self.name} поработал и заработал {earned_money} грн. Энергия: {self.energy}")
        else:
            print("Студенту нужно отдохнуть, чтобы продолжить работать или учиться.")

    def study(self):
        if self.energy > 70:
            self.grades += random.randint(5, 10)
            self.energy -= 10
            print(f"{self.name} занимался и улучшил успеваемость до {self.grades}. Энергия: {self.energy}")
        else:
            print("Студенту нужно отдохнуть, чтобы продолжить работать или учиться.")

    def rest(self):
        if self.money >= 5000:
            self.money -= 5000
            self.energy = min(100, self.energy + 40)
            self.turn_counter = 0
            print(f"{self.name} отдыхал и восстановил силы. Энергия: {self.energy}")
        else:
            print(f"У {self.name} недостаточно денег для отдыха. Деньги: {self.money}")

    def display_stats(self):
        print(f"\nХарактеристики студента {self.name}:")
        print(f"Успеваемость: {self.grades}")
        print(f"Деньги: {self.money} грн")
        print(f"Энергия: {self.energy}\n")

    def choose_action(self):
        self.turn_counter += 1
        if self.turn_counter == 4:
            print("Студенту нужно отдохнуть, чтобы продолжить работать или учиться.")
            while True:
                choice = input("Введите '3', чтобы отдохнуть: ")
                if choice != '3':  # Перевірка на правильний ввід
                    print("Неправильный ввод. Попробуйте еще раз.")
                else:
                    self.rest()
                    break

        print("Что вы хотите сделать?")
        print("1 - Пойти на работу")
        print("2 - Учиться")
        print("3 - Отдыхать")
        choice = input("Введите номер действия: ")

        if choice == "1":
            self.work()
        elif choice == "2":
            self.study()
        elif choice == "3":
            self.rest()
        else:
            print("Неверный выбор. Попробуйте снова.")
            self.choose_action()

    def live_a_year(self):
        for month in range(12):
            print(f"\nМесяц {month + 1}:")
            self.display_stats()
            self.choose_action()
            self.grades -= 5
            if self.grades < 0:
                self.grades = 0

            print(f"Итог месяца {month + 1}: Успеваемость: {self.grades}, Деньги: {self.money} грн, Энергия: {self.energy}")

student = Student(name="Алексей")
student.live_a_year()


