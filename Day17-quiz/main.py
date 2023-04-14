from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print('''  \033[36m
   ██████╗ 	██╗   ██╗  ██╗  ███████╗
  ██╔═══██╗	██║   ██║  ██║  ╚══███╔╝
  ██║   ██║	██║   ██║  ██║    ███╔╝ 
  ██║▄▄ ██║	██║   ██║  ██║   ███╔╝  
  ╚██████╔╝	╚██████╔╝  ██║  ███████╗
   ╚══▀▀═╝ 	 ╚═════╝   ╚═╝  ╚══════╝		\033[0m
''')

question_bank = []
# the above list of objects will look like 👇
# question_bank = [
	# new_question("A slug's blood is green.", "True"),
	# new_question("The loudest animal is the African Elephant.", "False"),
	# .
	# .
	# .
	# new_question("A few ounces of chocolate can kill a small dog.", "True"),
# ]

for question in question_data:
	question_text = question["question"]
	question_answer = question["correct_answer"]
	# create object of Question class,and pump
	# questions and answers as arguments from question_data list from data.py module
	new_question = Question(question_text, question_answer)	
	# adding above object to question_bank actually append()
	question_bank.append(new_question)

# print(question_bank[0]) 			# prints object details that is at 0th position in question_bank list
# print(question_bank[0].text)		# prints question of object that is at 0th position in question_bank list
# print(question_bank[0].answer)	# prints answer of object that is at 0th position in question_bank list

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
	quiz.next_question()

print("You have completed the Quiz.")
print(f"Your final score was : {quiz.score}/{quiz.question_number}")