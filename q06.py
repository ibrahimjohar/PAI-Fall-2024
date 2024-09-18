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


def main():
    manager = Manager("John Doe", 100000)
    developer = Developer("Jane Doe", 80000)
    senior_manager = SeniorManager("Bob Smith", 120000)

    print(f"Manager Bonus: ${manager.calculate_bonus():.2f}")
    manager.hire()

    print(f"\nDeveloper Bonus: ${developer.calculate_bonus():.2f}")
    developer.write_code()

    print(f"\nSenior Manager Bonus: ${senior_manager.calculate_bonus():.2f}")
    senior_manager.hire()


if __name__ == "__main__":
    main()