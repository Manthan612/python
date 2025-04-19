import uuid

class Student:
    def __init__(self, stu_id, name, age):
        self.uid = uuid.uuid4()
        self.stu_id = stu_id
        self.name = name
        self.age = age

    def display_info(self):
        print("\n----- Student Details -----")
        print(f"Unique UID     : {self.uid}")
        print(f"Student ID     : {self.stu_id}")
        print(f"Student Name   : {self.name}")
        print(f"Student Age    : {self.age}")

students = []

n = int(input("Enter the numbers of student in class: "))

for i in range(n):
    print(f"\nEntering details for Student {i+1}: ")
    stu_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    
    student = Student(stu_id, name, age)
    students.append(student)

print("ALL STUDENT DETAILS:")

for student in students:
    student.display_info()
