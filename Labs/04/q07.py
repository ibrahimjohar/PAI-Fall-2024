#name: ibrahim johar farooqi
#date: 11 september 2024
#lab: 04
#task: 7

class Vehicle:
    seating_capacity = 0

    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def calculate_fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def calculate_fare(self):
        total_fare = super().calculate_fare()
        return total_fare + (total_fare * 0.1)

school_bus = Bus(60)
print(f"total bus fare is: {school_bus.calculate_fare()}")
