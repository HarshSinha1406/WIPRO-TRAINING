class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print()


student1 = Student("Rahul", 101)
student2 = Student("Anita", 102)

student1.display_details()
student2.display_details()
