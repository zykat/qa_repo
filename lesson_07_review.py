### FILES #####
'''
Collect all warning logs from one file and save them in another file
'''

# log_file = "all.log"
# warning_logfile = "warning.log"
#
# warnings = []
# with open(log_file, 'r') as file:
#     for line in file.readlines():
#         if "WARNING" in line:
#             warnings.append(line)
# with open (warning_logfile, 'w') as file:
#     for item in warnings:
#         file.write(item)
#
# log_file = "all.log"
# warning_logfile = "warning.log"
# warnings = []
# with open(log_file, 'r') as file:
#     for line in file.readlines():
#         if "WARNING" in line:
#            with open (warning_logfile, 'a') as warning_file:
#                 warning_file.write(line)
#
#
### OOP ###
#
# Abstraction
#
# class Cat:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         print(f'Cat {self.name} is being initialized and meowing')
#     def say_meow(self):
#         print(f'{self.name} says MEOW!')
#     def print_name(self):
#         print("This is", self.name)
#     def print_age(self):
#         print(f'{self.name} is {self.age} years old')
#     def print_weight(self):
#         print(f"{self.name}'s weight is {self.weight} pounds")
#     def eat(self,food):
#         print(f'{self.name} ate {food}')
#     def eat_a_lot(self,food):
#         self.weight += 0.25
#         print(f'{self.name} ate a lot of {food} and gained qouter pound')

# black_cat - instance of a class - объект класса
# def - method of a class
# black_cat = Cat("Tom", 2, 8)
# print(black_cat)
# black_cat.print_name()
# black_cat.print_age()
# black_cat.print_weight()
# black_cat.say_meow()
# black_cat.eat("fish")
# black_cat.eat_a_lot("chicken")
# black_cat.print_weight()
#
# gray_cat = Cat("Lucky", 3, 14)
# print(gray_cat)
###
# Incapsulation
#
## public, protected, private
# class Person:
#     def __init__(self, name, dob, height, gender):
#         self._name = name
#         self.__dob = dob
#         self.height = height
#         self.gender = gender
#
#     def get_name(self):
#         return self._name
#     def get_dob(self):
#         return self.__dob
#     def set_dob(self, new_dob):
#         self.__dob = new_dob
#
# person_one = Person("John", "May 1, 2000", 6, "M")
# print(person_one.get_name())
# print(person_one.get_dob())
# person_one.set_dob("September 25, 2015")
# print(person_one.get_dob())

## protected - _name - may be parented through class
## private - __dob - in the class
###
# Inheritance
# # Polygon - parent class
# class Polygon:
#     def __init__(self, sides_count):
#         print("start init Polygon")
#         self.sides_count = sides_count
#         #self.color = color
#         print("stop init Polygon")
#     def print_number_of_sides(self):
#         print(f'It has {self.sides_count} sides')
#     def print_color(self):
#     return self.color

# Triangle - child class 1
# class Triangle(Polygon):
#     def __init__(self):
#         print("start init Triangle")
#         super().__init__(3)
#         print("stop init Triangle")
#
# class ColoredTriangle(Triangle):
#     def __init__(self, color):
#         print("start init ColoredTriangle")
#         super().__init__()
#         self.color = color
#         print("stop init ColoredTriangle")
#     def get_color(self):
#         return self.color

# tri = Triangle()
# tri.print_number_of_sides()

# red_tri = ColoredTriangle("red")
###
# Polymorphism
#
class Polygon:
    def __init__(self, sides_count):
        print("start init Polygon")
        self.sides_count = sides_count
        print("stop init Polygon")
    def print_number_of_sides(self):
        print(f'It has {self.sides_count} sides')

class Triangle(Polygon):
    def __init__(self, side_length):
        print("start init Triangle")
        super().__init__(3)
        self.side_length = side_length
        print("stop init Triangle")
    def print_number_of_sides(self):
        print(f'Of course it has {self.sides_count} sides, cuz this is triangle')

class ColoredTriangle(Triangle):
    def __init__(self, color):
        print("start init ColoredTriangle")
        super().__init__(55)
        self.color = color
        print("stop init ColoredTriangle")
    def get_color(self):
        return self.color

penta = Polygon(5)
penta.print_number_of_sides()

tri = ColoredTriangle('red')
tri.print_number_of_sides()
