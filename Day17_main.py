from Day17_QuestionModel import Question
from Day17_data import question_data
from Day17_QuizBrain import QuizBrain

question_bank = []
for item in question_data:
    try:
        question = Question(item["text"], item["answer"])
        question_bank.append(question)
    except KeyError:  #if question data does not have text or answer keys
        print("Missing key in question data.")
        continue

quiz = QuizBrain(question_bank)

while quiz.still_has_questions(): 
    quiz.new_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}.")
