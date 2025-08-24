📘 Python OOP Assignment – Class Design & Polymorphism
Author: Mawunyo Mary Fevlo

24th August, 2025

Objective: Demonstrate object-oriented programming concepts in Python through custom class creation and polymorphism.

Part 1: Custom Class – Smartphone

This section showcases a user-defined class called Smartphone, designed to represent basic features of a mobile device.

Features:

Attributes: brand, model, storage_gb

Methods:

turn_on() – Simulates powering on the phone

make_call(number) – Simulates making a call

get_info() – Returns device details

Sample Usage:

phone1 = Smartphone("Samsung", "Galaxy S23", 256)
phone2 = Smartphone("Apple", "iPhone 16", 128)

print(phone1.get_info())
phone2.make_call("0207923266")

Part 2: Polymorphism Challenge – Vehicle, Car, Plane

This section demonstrates polymorphism using a base class Vehicle and two subclasses Car and Plane, each overriding the move() method.

Features:

Parent Class: Vehicle with abstract method move()

Child Classes:

Car – Implements move() as "Driving 🚗"

Plane – Implements move() as "Flying ✈️"

Sample Usage:

vehicles = [Car(), Plane()]
for v in vehicles:
    print(v.move())

File Structur
Python_OOP_Assignment/
├── README.md
├── smartphone/
|   ├── __init__.py 
    |__ smartphone_class.py
├── Vehicles/
    ├── __init__.py 
    |__ polymorphism_challenge.py
├──tests/
    |__ test_smartphone.py
    |__ test_vehicles.py
| run_all.py 