students = {
    101: {"name": "Arjun", "marks": 85},
    102: {"name": "Rahul", "marks": 72},
    103: {"name": "Ananya", "marks": 94}
}

# 1. Display all students
print("--- 1. All Students ---")
for roll, info in students.items():
    print(f"Roll No: {roll} | Name: {info['name']} | Marks: {info['marks']}")

# 2. Search for a student using roll number
print("\n--- 2. Search Student (Roll 102) ---")
search_roll = 102
if search_roll in students:
    student = students[search_roll]
    print(f"Found! Name: {student['name']}, Marks: {student['marks']}")
else:
    print("Student not found.")