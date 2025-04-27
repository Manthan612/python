import uuid

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.student_id = str(uuid.uuid4())[:8]  # short unique ID

    def show_student_info(self):
        self.show_person_info()
        print(f"Student ID: {self.student_id}")

name = input("Enter student name: ")
age = int(input("Enter age: "))

s = Student(name, age)
print("\nStudent Info:")
s.show_student_info()




# class Device:
#     def __init__(self, brand):
#         self.brand = brand

#     def power_on(self):
#         print(f"{self.brand} device is now ON.")

# class Mobile(Device):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model

#     def show_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")

# m = Mobile("Samsung", "Galaxy S23")
# m.power_on()         # Parent class ka method
# m.show_info()        # Child class ka method