"""
Create a python program named as student_grade_calculator that takes a student's name and their grades for 5 subjects as input. 
The program should calculate the average grade and then classify it into grades:
 - A: 90-100
 - B: 80-89
 - C: 70-79
 - D: 60-69
 - F: below 60

Requirements:
 - Use string manipulation to format the student's name.
 - Use a list to store the grades.
 - Use flow control to classify the average grade.
 - Use a function to calculate the average and return the letter grade.
     
Sample Input:
Enter the student name: Zahid

Enter grades for subject 1: 94
Enter grades for subject 2: 91
Enter grades for subject 3: 77
Enter grades for subject 4: 88
Enter grades for subject 5: 66

Student Name is: Zahid
Highest Grade = 94.0
Lowest Grade = 66.0
Average: 83.2, which corresponds to: B

"""

# Solution:
def calculate_average (student_grades):
     # find the average
     avg = sum(student_grades) / len(student_grades)
     
     # find lowest and highest grades
     max_grade = student_grades[0]
     min_grade = student_grades[0]
     
     for grade in student_grades:
          if grade > max_grade:
               max_grade = grade
          if grade < min_grade:
               min_grade = grade
     
     # average classification
     letter_grade = ''
     if avg >= 90 and avg <= 100:
          letter_grade = 'A'   
     elif avg >= 80 and avg <= 89:
          letter_grade = 'B'
     elif avg >= 70 and avg <= 79:
          letter_grade = 'C'
     elif avg >= 60 and avg <= 69:
          letter_grade = 'D'
     else:
          letter_grade = "F"
     
     return max_grade, min_grade, avg, letter_grade


student_name = input("\nEnter the student name: ")
print()
student_grades = []

# assuming only 5 subjects are needed
for i in range(5):
     grade = float(input(f"Enter grades for subject {i+1}: "))
     student_grades.append(grade)

max_grade, min_grade, avg, letter_grade = calculate_average(student_grades)
print(f"\nStudent Name is: {student_name}")
print(f"Highest Grade = {max_grade}")
print(f"Lowest Grade = {min_grade}")
print(f"Average: {avg}, which corresponds to: {letter_grade}")




