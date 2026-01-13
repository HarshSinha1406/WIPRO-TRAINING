students = {
    "name": "Harsh",
    "age": 23,
    "Course": "Python"
}
print(students)
print(students["name"])
print(students.get("age"))
students["Marks"] = 85
students["age"] = 25
print(students)
print(students["name"])
print(students.get("age"))
students.pop("age")
print(students)
students.popitem()
print(students)
print(students.keys())
print(students.values())

for key in students:
    print(key, students[key])
if "name" in students:
    print("key exists")
employees = {
    101: {"name": "leena", "salary": 2000},
    102: {"name": "leena", "salary": 2000},
}
print(employees[101]["name"])
