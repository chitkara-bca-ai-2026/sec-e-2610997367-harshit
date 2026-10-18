name = input("Enter Student Name : ")
roll_number = input("Enter Roll Number : ")

total = 0
failed = False

print("\n--- Enter Marks for 5 Subjects (0-100) ---")

for i in range(1, 6):
    mark = int(input(f"Enter marks for Subject {i}: "))

    if mark < 0 or mark > 100:
        print("Invalid marks. Please enter marks from 0 to 100.")
        quit()

    total = total + mark

    if mark < 40:
        failed = True

percentage = total / 5

if failed:
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"
elif percentage >= 90:
    result = "PASS"
    grade = "A+"
    remark = "Outstanding"
elif percentage >= 80:
    result = "PASS"
    grade = "A"
    remark = "Excellent"
elif percentage >= 70:
    result = "PASS"
    grade = "B"
    remark = "Very Good"
elif percentage >= 60:
    result = "PASS"
    grade = "C"
    remark = "Good"
elif percentage >= 50:
    result = "PASS"
    grade = "D"
    remark = "Satisfactory"
else:
    result = "PASS"
    grade = "E"
    remark = "Pass"

print()
print("=" * 50)
print("             STUDENT REPORT CARD")
print("=" * 50)
print("Student Name :", name)
print("Roll Number  :", roll_number)
print("-" * 50)
print("Total Marks  :", total, "/ 500")
print("Percentage   :", format(percentage, ".2f") + "%")
print("Result       :", result)
print("Grade        :", grade)
print("Remarks      :", remark)
print("=" * 50)