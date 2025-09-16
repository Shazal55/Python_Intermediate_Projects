import csv
def grade_calculation(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

def calculate_percentage(obtained, out_of):
    return round((obtained / out_of) * 100, 2)

subjects = {}
number_of_subjects = int(input("Enter the Number of Subjects: "))
total_out_of_marks = 0

for i in range(number_of_subjects):
    subject_name = input("Enter the Subject Name: ").title()
    subject_total = int(input("Enter the Total Marks: "))
    subjects[subject_name] = subject_total
    total_out_of_marks += subject_total

with open("report_card.csv", "w", newline="") as file:
    writer = csv.writer(file)
    header = ["Name", "Roll No"] + list(subjects.keys()) + ["Total", "Percentage", "Grade"]
    writer.writerow(header)

should_continue = True
while should_continue:
    Total_marks_obtained = 0
    student_data = []
    student_name = input("\nEnter the Student Name: ").title()
    student_roll_no = input("Enter the Student Roll No: ")
    student_data.append(student_name)
    student_data.append(student_roll_no)

    for subject, total_marks in subjects.items():
        while True:
            try:
                obtained = int(input(f"Enter marks obtained in {subject} (out of {total_marks}): "))
                if 0 <= obtained <= total_marks:
                    Total_marks_obtained += obtained
                    student_data.append(obtained)
                    break
                else:
                    print(f"Marks must be between 0 and {total_marks}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    student_data.append(Total_marks_obtained)
    percentage_obtained = calculate_percentage(Total_marks_obtained, total_out_of_marks)
    grade = grade_calculation(percentage_obtained)
    student_data.append(percentage_obtained)
    student_data.append(grade)

    with open("report_card.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(student_data)
    wanna_continue = input("\nAdd another student? (Y/N): ").lower()
    if wanna_continue == "n":
        should_continue = False