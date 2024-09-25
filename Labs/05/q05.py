#name: ibrahim johar farooqi
#date: 18 september 2024
#lab: 05
#task: 5

from abc import ABC, abstractmethod
from datetime import datetime

class Vehicle(ABC):
    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
        self.rental_price = rental_price
        self.availability = True

    @abstractmethod
    def display_details(self):
        pass

    def check_availability(self):
        return self.availability

    def rent_vehicle(self):
        if self.availability:
            self.availability = False
            return True
        else:
            return False

    def return_vehicle(self):
        self.availability = True

    def calculate_rental_cost(self, rental_period):
        return self.rental_price * rental_period


class Car(Vehicle):
    def __init__(self, make, model, rental_price, num_doors):
        super().__init__(make, model, rental_price)
        self.num_doors = num_doors

    def display_details(self):
        print(f"make: {self.make}, model: {self.model}, rental price: ${self.rental_price}, number of doors: {self.num_doors}")


class SUV(Vehicle):
    def __init__(self, make, model, rental_price, seating_capacity):
        super().__init__(make, model, rental_price)
        self.seating_capacity = seating_capacity

    def display_details(self):
        print(f"make: {self.make}, model: {self.model}, rental price: ${self.rental_price}, seating capacity: {self.seating_capacity}")


class Truck(Vehicle):
    def __init__(self, make, model, rental_price, cargo_capacity):
        super().__init__(make, model, rental_price)
        self.cargo_capacity = cargo_capacity

    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Rental Price: ${self.rental_price}, Cargo Capacity: {self.cargo_capacity}")


class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date

    def display_details(self):
        print(f"customer: {self.customer.name}, vehicle: {self.vehicle.make} {self.vehicle.model}, start date: {self.start_date}, end date: {self.end_date}")


class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.rental_history = []

    def display_rental_history(self):
        for reservation in self.rental_history:
            reservation.display_details()


def display_vehicle_details(vehicle):
    vehicle.display_details()


car = Car("Toyota", "Corolla", 40, 4)
suv = SUV("Honda", "CR-V", 60, 5)
truck = Truck("Ford", "F-150", 80, 1000)

customer = Customer("Ibrahim Johar", "ibrahimjohar@gmail.com")

reservation1 = RentalReservation(customer, car, datetime(2023, 3, 1), datetime(2023, 3, 5))
reservation2 = RentalReservation(customer, suv, datetime(2023, 4, 1), datetime(2023, 4, 5))

customer.rental_history.append(reservation1)
customer.rental_history.append(reservation2)

print("vehicle details:")
display_vehicle_details(car)
display_vehicle_details(suv)
display_vehicle_details(truck)

print("\nrental reservations:")
reservation1.display_details()
reservation2.display_details()

print("\ncustomer rental history:")
customer.display_rental_history()
