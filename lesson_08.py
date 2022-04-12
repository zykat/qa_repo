### OOP in PYTHON ###
# Object Oriented Programming:
# - Inheritance
# - Abstraction
# - Encapsulation
# - Polymorphism
#
### Classes ###
# class Person:
#     name = ""
#     dob = ""
#     # class method
#     def age(self):
#         return "test age 30"
#     def get_age(self):
#         print(self.age())
#
# person_1 = Person()
# person_1.name = "Ali"
# person_1.dob = 12/4/1999
# # person_1.age = 34
# # print(person_1.name,person_1.age)
# ### age -> get_age -> person_1.get_age() ###
# person_1.get_age()
#
#### INHERETANCE ####
#
#
# # Polygon - parent class
# class Polygon:
#     def get_sides(self):
#         pass
#     sides_count = None
#
# # Triangle - child class 1
# class Triangle(Polygon):
#     def __init__(self):
#         self.sides_count = 3
#     def get_sides(self):
#         print(f"It has {self.sides_count} sides")
#
# # Pentagon - child class 2
# class Pentagon(Polygon):
#     def __init__(self):
#         self.sides_count = 5
#     def get_sides(self):
#         print(f"It has {self.sides_count} sides")
#
# Poly = Polygon()
# Poly.get_sides()
#
# T = Triangle()
# T.get_sides()
#
# P = Pentagon()
# P.get_sides()

# class Table():
#     # vstroennii method
#     def __init__(self, color, shape):
#         self.color = color
#         self.shape = shape
#
#     # class attribute
#     my_property = "test attribute"
#
#     # class method
#     def get_my_property(self):
#         print(self.my_property)
# my_table = Table("red", "oval")
#
# my_table.get_my_property()
# print(my_table.color)
# print(my_table.shape)
### HOMEWORK ####
"""
8.1 Use an object from the real world to create a class in Python
"""
class Planets:
    def __init__(self, name,radius,temp):
        self.name = name
        self.radius = radius
        self.temp = temp

    def get_name(self):
        print(f'This is planet: {self.name}')

    def get_radius(self):
        print(f'{self.name} has {self.radius} mi ')

    def get_temp(self):
        print(f'Temperature: {self.temp} Celsius')

print('_________++++++++______________')
planet_1 = Planets('Venus', 3.760, 475)
planet_1.get_name()
planet_1.get_radius()
planet_1.get_temp()
print('_________++++++++______________')

planet_2 = Planets('Mars',2.106 , -220)
planet_2.get_name()
planet_2.get_radius()
planet_2.get_temp()
print('_________++++++++______________')

planet_3 = Planets('Mercury', 1.516, 427)
planet_3.get_name()
planet_3.get_radius()
planet_3.get_temp()
print('_________++++++++______________')


