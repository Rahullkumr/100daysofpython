"""
You have access to a database of student_scores in the format of a dictionary. 
The keys in student_scores are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. 
By the end of your program, you should have a new dictionary called student_grades 
that should contain student names for keys and their grades for values. 

The final version of the student_grades dictionary will be checked.

This is the scoring criteria:
	Scores 91 - 100: Grade = "Outstanding"
	Scores 81 - 90: Grade = "Exceeds Expectations"
	Scores 71 - 80: Grade = "Acceptable"
	Scores 70 or lower: Grade = "Fail"
"""

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if (student_scores[key] >= 91) and (student_scores[key] <=100):
        student_grades[key] = "Outstanding"
    elif (student_scores[key] >= 81) and (student_scores[key] <=90):
        student_grades[key] = "Exceeds Expectations"
    elif (student_scores[key] >= 71) and (student_scores[key] <=80):
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)