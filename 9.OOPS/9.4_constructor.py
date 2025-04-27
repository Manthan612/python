'''
__init()

1-> default(self)
2-> parameterized(self,name,colour)
3-> constructor with default value(self,name='Unknon',age=0)


'''

# class Car:
#     def set_details(self,colour,name):
#         print(f'car {name} with {colour} Colour'.title())

# c1 = Car()
# c1.set_details('Black','G Wagon')

class Car:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
c1 = Car('Tesla','Black')
c2 = Car('BMW','White')

print(f'Car {c1.name} With {c1.colour} Colour')
print(f'Car {c2.name} With {c2.colour} Colour')