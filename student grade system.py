print("Student Result System")
students = {"Amit": 85, "Priya": 92, "Rahul": 78, "Neha": 88}
total_marks = sum(students.values())
average = total_marks / len(students)
print(f"Average Marks: {average}")
topper_name = ""
highest_mark = 0
for name, mark in students.items():
    if mark > highest_mark:
        highest_mark = mark
        topper_name = name
print(f"Topper: {topper_name} with {highest_mark} marks")
grades = [f"{name}: A" if mark >= 80 else f"{name}: B" for name, mark in students.items()]
print("Grades:", grades)