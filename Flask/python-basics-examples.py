# Defining a class
# You can run this by 
# https://medium.freecodecamp.org/learning-python-from-zero-to-hero-120ea540b567

# Python has the concept of multi-inheritance.


class Vehicle:
    def __init__(self, car_type = "Sedan"):
        self.model_type = car_type
    
    # This becomes a getter
    @property
    def model_type(self):
        return self.model_type
    
    # This is how you can define getters and setters
    # This becomes a setter
    @model_type.setter
    def model_type(self, car_type):
        self.model_type = car_type

class Vehicle2:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    @property
    def number_of_wheels(self):
        return self._number_of_wheels

    @number_of_wheels.setter
    def number_of_wheels(self, number):
        self._number_of_wheels = number

vehicle = Vehicle2(4, "Super", "17", "40 Km/h")
# print(vehicle.type)
print(vehicle.number_of_wheels)
