#name: ibrahim johar farooqi
#date: 18 september 2024
#lab: 05
#task: 6

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        pass


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary * 0.2

    def hire(self):
        print(f"{self.name} is hiring someone.")


class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary * 0.1

    def write_code(self):
        print(f"{self.name} is writing code.")


class SeniorManager(Manager):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary * 0.3


manager = Manager("johar", 80000)
developer = Developer("farooqi", 60000)
senior_manager = SeniorManager("ibrahim", 100000)

print(f"{manager.name}'s bonus: ${manager.calculate_bonus()}")
manager.hire()

print(f"{developer.name}'s bonus: ${developer.calculate_bonus()}")
developer.write_code()

print(f"{senior_manager.name}'s bonus: ${senior_manager.calculate_bonus()}")
