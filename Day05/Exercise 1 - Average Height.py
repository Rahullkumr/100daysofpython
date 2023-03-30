'''
You are going to write a program that calculates 
the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

You should not use the sum() or len() functions in your answer. 
You should try to replicate their functionality using for loops.

'''

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
count = 0

for sh in student_heights:
    sum += sh   
    count += 1

average = round(sum/count)
print(average)