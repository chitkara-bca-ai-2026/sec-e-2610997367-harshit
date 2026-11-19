students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "2",
        "Marks": [85, 90, 78],
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [92, 88, 95],
    },
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82],
    },
}


def show_menu():
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")


def show_student(roll, student):
    print(f"Roll No: {roll} | Name: {student['Name']:<10} "
          f"| Branch: {student['Branch']} | Sem: {student['Semester']} "
          f"| Marks: {student['Marks']}")


def read_marks():
    marks = []
    for subject in range(1, 4):
        while True:
            try:
                mark = int(input(f"  Subject {subject}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Enter a mark from 0 to 100.")
            except ValueError:
                print("Enter a whole number.")
    return marks


while True:
    show_menu()
    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        print("\n--- Enrolled Student Records ---")
        if not students:
            print("No student records found.")
        else:
            for roll, student in students.items():
                show_student(roll, student)
        print(f"Total Enrolled Students: {len(students)}")

    elif choice == "2":
        roll = input("Enter Roll Number to search: ").strip()
        student = students.get(roll)

        if student is None:
            print(f"[ERROR] No student found with Roll No {roll}.")
        else:
            print(f"\n[FOUND] Record for Roll No {roll}:")
            print(f"  Name     : {student['Name']}")
            print(f"  Branch   : {student['Branch']}")
            print(f"  Semester : {student['Semester']}")
            print(f"  Marks    : {student['Marks']}")

    elif choice == "3":
        print("\n--- Register New Student ---")
        roll = input("Enter Roll Number: ").strip()

        if not roll:
            print("[ERROR] Roll Number cannot be empty.")
            continue
        if roll in students:
            print(f"[ERROR] Roll Number {roll} already exists.")
            continue

        name = input("Enter Student Name: ").strip()
        branch = input("Enter Branch (e.g. BCA AI): ").strip()
        semester = input("Enter Semester: ").strip()

        if not name or not branch or not semester:
            print("[ERROR] Name, Branch, and Semester are required.")
            continue

        print("Enter marks obtained in 3 subjects:")
        marks = read_marks()

        students[roll] = {
            "Name": name,
            "Branch": branch,
            "Semester": semester,
            "Marks": marks,
        }
        print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) "
              "registered successfully.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ").strip()
        student = students.get(roll)

        if student is None:
            print(f"[ERROR] No student found with Roll No {roll}.")
            continue

        print(f"Current details for {student['Name']} (Roll {roll}):")
        print(f"1. Branch: {student['Branch']} | "
              f"2. Semester: {student['Semester']}")

        field_choice = input(
            "Choose field to update (1 for Branch, 2 for Semester): "
        ).strip()

        if field_choice == "1":
            new_branch = input("Enter new branch: ").strip()
            if new_branch:
                student["Branch"] = new_branch
                print(f"[SUCCESS] Branch updated to '{new_branch}'.")
            else:
                print("[ERROR] Branch cannot be empty.")
        elif field_choice == "2":
            new_semester = input("Enter new semester: ").strip()
            if new_semester:
                student["Semester"] = new_semester
                print(f"[SUCCESS] Semester updated to '{new_semester}'.")
            else:
                print("[ERROR] Semester cannot be empty.")
        else:
            print("[ERROR] Choose 1 for Branch or 2 for Semester.")

    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ").strip()
        student = students.get(roll)

        if student is None:
            print(f"[ERROR] No student found with Roll No {roll}.")
            continue

        total = sum(student["Marks"])
        maximum = len(student["Marks"]) * 100
        average = total / len(student["Marks"])
        result = "PASS" if average >= 40 else "FAIL"

        print("\n=============== ACADEMIC REPORT ===============")
        print(f"Student Name : {student['Name']} (Roll: {roll})")
        print(f"Subject Marks: {student['Marks']}")
        print(f"Total Marks  : {total} / {maximum}")
        print(f"Average Marks: {average:.2f}%")
        print(f"Final Result : {result}")
        print("=" * 48)

    elif choice == "6":
        roll = input("Enter Roll Number to delete: ").strip()
        deleted_student = students.pop(roll, None)

        if deleted_student is None:
            print(f"[ERROR] No student found with Roll No {roll}.")
        else:
            print(f"[SUCCESS] Record for '{deleted_student['Name']}' "
                  f"(Roll No: {roll}) deleted successfully.")

    elif choice == "7":
        print("\nThank you for using Student Information System.")
        print("Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 7.")