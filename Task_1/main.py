student_marks = {
    "Alice": 85,
    "Mark": 90,
    "Charlie": 33,
    "Diana": 88,
    "Ethan": 79
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Sorry, {student_name} is not found in the records.")