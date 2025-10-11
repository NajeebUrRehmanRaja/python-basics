students = {
    "name": "John Doe",
    "age": 20,
    "grade": "A"
}

print(students["name"])

print(students.pop("age"))

print(students)

print(students.keys())

print(students.values())

del students["grade"]

print(students)

students.update({"age": 21})

print(students)

for key, value in students.items():
    print(key, value)
