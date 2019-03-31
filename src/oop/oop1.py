# Write classes for the following class hierarchy:
class Vehicle:
    pass

class FlightVehicle(Vehicle):
    pass

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass

class GroundVehicle(Vehicle):
    pass
#base class is vehicle

class Car(GroundVehicle):
    pass
#base class is ground vehicle

class Motorcycle(GroundVehicle):
    pass
# base class is ground vehicle

#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
