#Mini Project: Grading system: Take user marks and print the grade.

marks = float(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter between 0 and 100.")

elif marks >= 80:
    print("Grade: A+")

elif marks >= 70:
    print("Grade: A")

elif marks >= 60:
    print("Grade: B")

elif marks >= 50:
    print("Grade: C")

elif marks >= 40:
    print("Grade: D")

else:
    print("Grade: F")
